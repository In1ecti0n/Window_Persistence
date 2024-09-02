Set-ExecutionPolicy Bypass

function NewService {
    param (
        $name,
        $nameDisplay,
        $path,
        $description,
        $type
    )
    New-Service -Name $name -DisplayName $nameDisplay -BinaryPathName $path -Description $description -StartupType $type
}

$name = Read-Host "New service:"
$nameDisplay = Read-Host "New display name service:"
$path = Read-Host "New path name:"
$description = Read-Host "New description:"
$type = Read-Host "New startup type [Automatic; Manual; Disable;]:"

NewService -name $name -nameDisplay $nameDisplay -path $path -description $description -type $type





