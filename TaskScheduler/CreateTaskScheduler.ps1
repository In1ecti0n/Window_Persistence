Set-ExecutionPolicy Bypass

function CreateTaskScheduler {
    param (
        $name,
        $path,
        $argument = " ",
        $time
    )
    $action = New-ScheduledTaskAction -Execute $path -Argument $argument 
    $trigger = New-ScheduledTaskTrigger -Daily -At $time
    Register-ScheduledTask -TaskName $name -Action $action -Trigger $trigger -RunLevel Highest
}

$name = Read-Host "Please enter task name:"
$path = Read-Host "Please enter program's path:"
$argument = Read-Host "Argument ?:"
$time = Read-Host "Time (like 00:00:10):"
CreateTaskScheduler -name $name -path $path -argument $argument -time $time

