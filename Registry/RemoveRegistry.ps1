Set-ExecutionPolicy Bypass

function Delete_Key {
    param (
        $path
    )
    Remove-Item -Path $path -Recurse
}

function Delete_Value {
    param (
        $name,
        $path
    )
    Remove-ItemProperty -Path $path -Name $name
}


Write-Host "Delete Key (1) or Value (2), please choose?"
$choose = Read-Host "1 or 2:"
if ($choose -eq 1){
    $path = Read-Host "Path need to delete:"
    Delete_Key -path $path
}elseif ($choose -eq 2){
    $path = Read-Host "Path need tp delete:"
    $name = Read-Host "Name:"
    Delete_Value -path $path -name $name
}