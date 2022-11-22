 $folder = '..\..\Work\Zip\DECRYPT' # Enter the root path you want to monitor. 
 $filter = '*.zip'  # You can enter a wildcard filter here. 

 $fsw = New-Object IO.FileSystemWatcher $folder, $filter -Property  @{IncludeSubdirectories = $true;NotifyFilter = [IO.NotifyFilters]'FileName, LastWrite'}

 Register-ObjectEvent $fsw Created -SourceIdentifier FileCreated -Action { 
 $name = $Event.SourceEventArgs.Name 
 $changeType = $Event.SourceEventArgs.ChangeType 
 $timeStamp = $Event.TimeGenerated 
 Write-Host "The file '$name' was $changeType at $timeStamp" -fore green
    Invoke-Item '..\..\Work\Zip\decrypt.exe'
 }