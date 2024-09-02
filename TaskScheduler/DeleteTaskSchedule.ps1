Set-ExecutionPolicy Bypass
$name = Read-Host "Please enter task name:"
Unregister-ScheduledTask -TaskName $name -Confirm:$false
Write-Host "Delete successfully!"