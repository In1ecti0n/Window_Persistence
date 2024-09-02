Set-ExecutionPolicy Bypass

function UpdateTask {
    param (
        $name,
        $path,
        $argument = " ",
        $time
    )
    $action = New-ScheduledTaskAction -Execute $path -Argument $argument
    $trigger = New-ScheduledTaskTrigger -Daily -At $time
    Set-ScheduledTask -TaskName $name -Action $action -Trigger $trigger

}

Write-Host "Update Task Scheduler!"
$name = Read-Host "Enter task name you want to update"
$path = Read-Host "New path:"
$argument = Read-Host "New argument:"
$time = Read-Host "New time startup:"
UpdateTask -name $name -path $path -argument $argument -time $time

