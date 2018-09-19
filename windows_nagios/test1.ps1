#获取本机内存大小，单位为Gb，小数点后保留两位
#$mem = "{0:N2}GB" -f (((Get-WmiObject -Class Win32_PhysicalMemory).capacity | Measure-Object -Sum).sum /1gb)
Get-WmiObject -Class Win32_PhysicalMemory | %{$sum = 0} { $sum += $_.Capacity }
$mem=$sum/1024/1024/1024
#$mem= Get-WmiObject -Class Win32_PhysicalMemory | %{$sum = 0} { $sum += $_.Capacity } {Write-Host ($sum / 1GB) }
#获取本机内存条数
#$slot = ((Get-WmiObject -Class Win32_PhysicalMemory).capacity | Measure-Object -Sum).count
$cpus=@(Get-WmiObject -Class Win32_Processor).count


if ($mem -eq 4 -and $cpus -eq 2 ) {
Write-Host "OK-本机共 $cpus 个CPU,内存 $mem 个G"

exit 0
}
else
{

Write-Host "Waring-本机共 $cpus 个CPU,内存 $mem 个G"
exit 2
}


#Write-Host "本机内存总计: $mem"
#Write-Host "本机共 $slot 条内存"

#@(Get-WmiObject -Class Win32_Processor).count

#Get-WmiObject -Class CIM_LogicalDevice | Out-GridView
#Get-WmiObject -Class CIM_LogicalDevice |
  Select-Object -Property __Class, Description |
  Sort-Object -Property __Class -Unique |
  Out-GridView



#$cpus=@(Get-WmiObject -Class Win32_Processor).count

#Write-Host "本机共 $cpus 个CPU"

#exit 0