#��ȡ�����ڴ��С����λΪGb��С���������λ
#$mem = "{0:N2}GB" -f (((Get-WmiObject -Class Win32_PhysicalMemory).capacity | Measure-Object -Sum).sum /1gb)
Get-WmiObject -Class Win32_PhysicalMemory | %{$sum = 0} { $sum += $_.Capacity }
$mem=$sum/1024/1024/1024
#$mem= Get-WmiObject -Class Win32_PhysicalMemory | %{$sum = 0} { $sum += $_.Capacity } {Write-Host ($sum / 1GB) }
#��ȡ�����ڴ�����
#$slot = ((Get-WmiObject -Class Win32_PhysicalMemory).capacity | Measure-Object -Sum).count
$cpus=@(Get-WmiObject -Class Win32_Processor).count


if ($mem -eq 4 -and $cpus -eq 2 ) {
Write-Host "OK-������ $cpus ��CPU,�ڴ� $mem ��G"

exit 0
}
else
{

Write-Host "Waring-������ $cpus ��CPU,�ڴ� $mem ��G"
exit 2
}


#Write-Host "�����ڴ��ܼ�: $mem"
#Write-Host "������ $slot ���ڴ�"

#@(Get-WmiObject -Class Win32_Processor).count

#Get-WmiObject -Class CIM_LogicalDevice | Out-GridView
#Get-WmiObject -Class CIM_LogicalDevice |
  Select-Object -Property __Class, Description |
  Sort-Object -Property __Class -Unique |
  Out-GridView



#$cpus=@(Get-WmiObject -Class Win32_Processor).count

#Write-Host "������ $cpus ��CPU"

#exit 0