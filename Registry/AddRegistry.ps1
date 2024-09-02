Set-ExecutionPolicy Bypass

function Add_Key {
    param (
        $path
    )
    New-Item -Path $path
}

function Add_Value {
    param (
        $path,
        $name,
        $value,
        $type
    )
    New-ItemProperty -Path $path -Name $name -Value $value -PropertyType $type -Force
}

# Set-Location -Path 'HKCU:\Software\Microsoft\Windows\CurrentVersion\Run'
$path= Read-Host "Enter key path:"
if (!(test-path $path)){
    New-Item -Path $path
}
$name = Read-Host "Enter name:"
$value = Read-Host "Enter value:"
Write-Host "Type data: String - MultiString - DWord - QWord - Binary"
$type = Read-Host "Type data:"
Add_Value -path $path -name $name -value $value -type $type 