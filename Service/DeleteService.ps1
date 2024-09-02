Set-ExecutionPolicy Bypass

function DeleteService {
    param (
        $nameService
    )
    sc.exe delete $nameService
    Write-Host "Delete successfully!"
}

$name = Read-Host "Please enter name service:"
DeleteService -nameService $name



