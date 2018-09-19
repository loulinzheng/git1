#!/usr/bin/perl
#Monitor VMware ESX hosts for operational indicators	S.Teeter   Aug-2010
#Purpose is to send results to Nagios using nsca
#$ARGV[0] contains a schedule name matching schedules in ESX_Hosts
#Print stmts are for debugging; formal output goes to nsca_vmware_$ARGV[0].dat
#See http://www.vmware.com/pdf/vsphere4/r41/vsp4_41_vcli_inst_script.pdf
#and http://www.vmware.com/pdf/vsphere4/r41/vsp_41_resource_mgmt.pdf
#Perl programmers, please forgive my perl; not my native language

#(1) Set required variables; alter as needed for local environment
$runtimer=time();
open (TMP, "date '+%F %H:%M:%S' |") || die "Failed on date: $!\n";
while ($line=<TMP>) { chomp($datetime=$line); }
close (TMP);
print "Starting execution of $0 v1.2.1 at $datetime\n";
$sched=$ARGV[0];	# schedule to run on this iteration
if ($sched eq "") { print "$0 requires a schedule name\n"; exit 1; }
if ($sched =~ m/\s/) { 
    print "schedule name cannot contain white space\n"; exit 2; }
print "... schedule is $sched\n";
$dir="/opt/nsca/VMware"; # location of components
$esx="ESX_Hosts";       # master file of ESX hosts to process
$pfx="nsca_vmware_";	# file name prefix for this schedule
$resx="esxtop4rc";	# resxtop minimal configuration file
$msglen=200;            # max length of status information msg
# Service names for Nagios; customize as needed
@service=("ESX-OVERCMMT",	# memory overcommit
	  "ESX-CPU-LOAD",	# CPU load average
	  "ESX-MEMORY",		# memory used %
	  "ESX-FILESYS",	# filesystem used %
	  "ESX-VM-STATE");	# VM count and states
# Warning and Critical levels for services above; customize as needed
@warn=(90,85,85,99,85);		# yellow alert; last entry is not used
@crit=(100,95,95,100,95);		# red alert; last entry is not used

#(2) Process file of ESX hosts
#    Format is hostname \t account \t password \t CPU/Mem \t FileSys \t VMcount
#    hostname is fully qualified, so use hostabbr for Nagios nsca
open (DAT, ">$dir/$pfx$sched.dat") 
    or die "Failed on open $pfx$sched.dat: $!\n";
open (ESX,"< $dir/$esx") or die "Failed on open $esx: $!\n";
while ($line=<ESX>) {
    chomp($string=$line);
    if (substr($string,0,1) eq "#") { next; }	# skip comments
    $hosttimer=time();
    @parm=split(/\t/,$string);
    if ($#parm<=2) { next; }			# skip hosts w/ no options
    if($parm[1] eq "!") { next; }		# skip hosts w/o root acct
    if (($#parm>2 && $parm[3] eq $sched)
	or ($#parm>3 && $parm[4] eq $sched)
	or ($#parm>4 && $parm[5] eq $sched)) { 
	print "Processing host $parm[0]\n"; }
    else { next; }				# skip hosts if nothing to do
    @parm2=split(/\./,$parm[0]);
    $hostabbr=$parm2[0];			# unqualify hostname
    if ($#parm>2 && $parm[3] eq $sched) { 
	&cpumem($parm[0],$parm[1],$parm[2]); }	# process CPU & memory
    if ($#parm>3 && $parm[4] eq $sched) { 
	&filesys($parm[0],$parm[1],$parm[2]); }	# process filesystems
    if ($#parm>4 && $parm[5] eq $sched) { 
	&vmcount($parm[0],$parm[1],$parm[2]); }	# process VMs on host
    $hosttimer=time()-$hosttimer;
    print "... host $hostabbr took $hosttimer seconds\n";
    } # end while ESX
close (ESX);
close (DAT);
$runtimer=time()-$runtimer;
print "$0 took $runtimer seconds\n";

#(3) Subroutine to check CPU and memory
sub cpumem {
    $subtimer=time();
    $overcommit=-1;			# memory overcommit
    $cpuload=-1;			# 5-min CPU load factor
    $memtot=-1;				# total memory
    $memfree=-1;			# free memory
    $cpuctr=0;				# CPU counter
    $linectr=0;				# line counter
#(a) Use 'resxtop' command to get memory and CPU measurements
# Password piped into resxtop to avoid prompt for it
    system ("echo $_[2] | resxtop -b -c $resx -n 1 --server $_[0] --user $_[1] 1>$dir/$pfx$sched.cmd 2>$dir/$pfx$sched.err");
#(b) Check for errors raised by command
    open (ERR,"< $dir/$pfx$sched.err") 
	or die "Failed on open $pfx$sched.err: $!\n";
    while ($line=<ERR>) {
	chomp($string=$line);
	if ($string =~ m/password: $/) { next; }	# expected
	if ($string =~ m/^\s*$/) { next; }		# blank line
	&print_results($hostabbr,$service[0],"3",$string);
	&print_results($hostabbr,$service[1],"3",$string);
	&print_results($hostabbr,$service[2],"3",$string);
	close (ERR); 
	return; 
	} # end while $line
	close (ERR);
#(c) Process command output
    open (CMD,"< $dir/$pfx$sched.cmd") 
	or die "Failed on open $pfx$sched.cmd: $!\n";
    while ($line=<CMD>) {
	chomp($string=$line);
	$string =~ s/"//g;		# remove quote marks
	@value=split(',',$string);	# comma delimited values
	++$linectr;
	$valctr=0;
	while ($linectr==1 && $valctr<=$#value) { # get posns from col headers
	    if ($value[$valctr] =~ m/Memory Overcommit \(5 Minute Avg\)/) {
		$overcommit=$valctr; ++$valctr; next; }
	    if ($value[$valctr] =~ m/Cpu Load \(5 Minute Avg\)/) {
		$cpuload=$valctr; ++$valctr; next; }
	    if ($value[$valctr] =~ m/\\Memory\\Machine MBytes/) {
		$memtot=$valctr; ++$valctr; next; }
	    if ($value[$valctr] =~ m/\\Memory\\Free MBytes/) {
		$memfree=$valctr; ++$valctr; next; }
	    if ($value[$valctr] =~ m/Physical Cpu\(\d+\)\\% Processor Time/) {
		++$cpuctr; ++$valctr; next; }
	    ++$valctr; next;
	    } # end while $linectr==1
	if ($linectr==2) {		# now get data using posns
	    if ($overcommit>-1)	{ $overcommit=$value[$overcommit]; }
	    if ($cpuload>-1)	{ $cpuload=$value[$cpuload]; }
	    if ($memtot>-1)	{ $memtot=$value[$memtot]; }
	    if ($memfree>-1)	{ $memfree=$value[$memfree]; }
	    } # end if $linectr==2
	} # end while $line=<CMD>
    close (CMD);
#(d) Format command results for nsca
    print "... overcommit $overcommit, cpuload $cpuload on $cpuctr cpus, memtot $memtot, memfree $memfree\n";
    if ($overcommit =~ m/[0-9.]+/ && $overcommit>-1) { # memory overcommitment
	$overcommit=$overcommit*100;
	$rc=($overcommit > $crit[0]) ? 2 : (($overcommit > $warn[0]) ? 1 : 0); 
	$msg="Memory overcommitment " . sprintf("%d",$overcommit) . "%"; }
    else { 
	$rc=3; 
	$msg="Memory overcommitment " . $overcommit; }
    &print_results($hostabbr,$service[0],$rc,$msg);
    if ($cpuload =~ m/[0-9.]+/ && $cpuload>-1) {	# print CPU loading
        $cpuload=$cpuload*100;
        $rc=($cpuload > $crit[1]) ? 2 : (($cpuload > $warn[1]) ? 1 : 0);
        $msg="CPU load average " . sprintf("%d",$cpuload) . "% on " . 
	    $cpuctr . " CPUs"; }
    else {
        $rc=3;
        $msg="CPU load average  " . $cpuload . " on " . $cpuctr ." CPUs"; }
    &print_results($hostabbr,$service[1],$rc,$msg);
    if ($memtot =~ m/[0-9.]+/ && $memfree =~ m/[0-9.]+/
	&& $memtot>-1 && $memfree>-1) { 		# print memory usage
        $memused=$memtot-$memfree;
        $memload=($memused/$memtot)*100;
        $rc=($memload > $crit[2]) ? 2 : (($memload > $warn[2]) ? 1 : 0);
        $msg="Memory use " . sprintf("%d",$memload) . "% (" . $memused . 
	    " of " . $memtot . " MB used)"; }
    else {
        $rc=3;
        $msg="Memory use " . $memtot . " total " .  $memfree . " free"; }
    &print_results($hostabbr,$service[2],$rc,$msg);
    $subtimer=time()-$subtimer;
    print "... mem/cpu took $subtimer seconds\n";
    } # end subroutine

#(4) Subroutine to check filesystems
sub filesys {
    $subtimer=time();
    @fsdata=();				# utilization \t label
    $fsctr=0;				# filesystem counter
#(a) Use 'vifs -listds' command to get list of all filesystems on host
    system ("vifs --server $_[0] --username $_[1] --password $_[2] --listds 1>$dir/$pfx$sched.cmd 2>$dir/$pfx$sched.err");
#(b) Check for errors raised by command
    open (ERR,"< $dir/$pfx$sched.err") 
	or die "Failed on open $pfx$sched.err: $!\n";
    while ($line=<ERR>) {
        chomp($string=$line);
	if ($string =~ m/^\s*$/) { next; }		# blank line
        &print_results($hostabbr,$service[3],"3",$string);
        close (ERR); 
	return; 
        } # end while $line
        close (ERR); 
#(c) Query each filesystem with 'vmkfstools --queryfs' and parse results
    open (CMD,"< $dir/$pfx$sched.cmd") 
	or die "Failed on open $pfx$sched.cmd: $!\n";
    while ($line=<CMD>) {
	++$fsctr;
        chomp($fsname=$line);
	open (TMP, "vmkfstools --server $_[0] --username $_[1] --password $_[2] --queryfs \"/vmfs/volumes/$fsname\" 2>&1 |");	# collect any error messages
	while ($line=<TMP>) {
            chomp($string=$line);
	    @word=split(' : ',$string);
	    if ($word[0] ne "Capacity") { next; }	# ignore other lines
	    $word[1] =~ s/,//;
	    @qty=split(' ',$word[1]);
	    if ($qty[0] !~ m/[0-9.]+/ || $qty[1] !~ m/[0-9.]+/) { next; }
	    if ($qty[0]==0) { next; }			# inactive
	    $util=($qty[0]-$qty[1])*100/$qty[0]; 
	    $fsdata[$fsctr]=sprintf("%03d",$util) . "\t" . $fsname;
	    } # end while $line=<TMP>
	close (TMP);
	} # end while $line=<CMD>
    close (CMD);
#(d) Sort by descending usage and format output
    @fsdata = reverse sort @fsdata;
    $rc=0;
#foreach (@fsdata) { print "$_\n"; }
    $msg="Of ". $fsctr . " filesystems, max usage is ";
    $punct="";
    foreach (@fsdata) { 
	@word=split(/\t/,$_);
	$msg=$msg . $punct . $word[1] . " (" . sprintf("%d",$word[0]) . "%)";
	$punct=", ";
	$rc=($word[0]>$crit[3]) ? 2 : (($word[0]>$warn[3] && $rc<2) ? 1 : $rc);
	} # end foreach @fsdata
    &print_results($hostabbr,$service[3],$rc,$msg);
    $subtimer=time()-$subtimer;
    print "... filesys took $subtimer seconds\n";
    } # end subroutine

#(5) Subroutine to check virtual machines
sub vmcount {
    $subtimer=time();
    $rc=0;
    @state=();				# array of states (on, off, etc.)
    @statectr=();			# array of state counters
    $vmctr=0;				# VM counter
#(a) Use 'vmware-cmd -l' command to get list of all VMs on host
    system ("vmware-cmd --server $_[0] --username $_[1] --password $_[2] -l 1>$dir/$pfx$sched.cmd 2>$dir/$pfx$sched.err");
#(b) Check for errors raised by command
    open (ERR,"< $dir/$pfx$sched.err") 
	or die "Failed on open $pfx$sched.err: $!\n";
    while ($line=<ERR>) {
        chomp($string=$line);
	if ($string =~ m/^\s*$/) { next; }		# blank line
        &print_results($hostabbr,$service[4],"3",$string);
        close (ERR); 
	return;
        } # end while $line
        close (ERR); 
#(c) Query each VM with 'vmware-cmd getstate' and parse results
    open (CMD,"< $dir/$pfx$sched.cmd") 
	or die "Failed on open $pfx$sched.cmd: $!\n";
    while ($line=<CMD>) {
        chomp($vmname=$line);
	if ($vmname !~ m/^\/vmfs\/volumes\//) { next; }	# blank or unexpected
        ++$vmctr;
        open (TMP, "vmware-cmd --server $_[0] --username $_[1] --password $_[2] \"$vmname\" getstate 2>&1 |");			# collect any error messages
        $line=<TMP>;				# get first line only
        chomp($string=$line);
	if ($string =~ m/getstate/) { @word=split(' = ',$string); }
	else { $word[1]="unknown"; }		# bad or missing data
	for ($i=0;$i<=$#state;++$i) { 
	    if ($word[1] eq $state[$i]) { ++$statectr[$i]; last; } }
	if ($i>$#state) { $state[$i]=$word[1]; $statectr[$i]=1; }
	close (TMP);
        } # end while $line=<CMD>
	close (CMD);
#(d) Format output
    if ($vmctr==0) { $msg="No virtual machines found"; $rc=1; }
    else { $msg="Of ". $vmctr . " virtual machines"; }
    for ($i=0;$i<=$#state;++$i) { 
	$vmchkr=$vmchkr+$statectr[$i];
	if ($statectr[$i]<2) {
	    $msg=$msg . ", " . $statectr[$i] . " is " . $state[$i]; }
	else { $msg=$msg . ", " . $statectr[$i] . " are " . $state[$i]; }
	} # end for i
    &print_results($hostabbr,$service[4],$rc,$msg);
    $subtimer=time()-$subtimer;
    print "... vmcount took $subtimer seconds\n";
    } # end subroutine

#(6) Subroutine to print formal and debugging outputs
sub print_results {
    $_[3]=~ s/ +/ /g; # remove extra spaces from msg
    if (length($_[3])>$msglen) { 	# truncate msg if required
	$_[3]=substr($_[3],0,$msglen-10) . " (more...)"; }
    printf "%s\t%s\t%d\t%s\n",$_[0],$_[1],$_[2],$_[3];
    printf DAT "%s\t%s\t%d\t%s\n",$_[0],$_[1],$_[2],$_[3];
    } # end subroutine
