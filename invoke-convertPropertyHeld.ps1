# Read all of the propertyheld csv files generated from camelot and combine 
# them into one file for each docket

$filelist = "248-blockfiintl-propertyheld", "262-walletllc-propertyheld"

foreach ($f in $filelist) {
    $inputfiles = Get-ChildItem -Path ./output-stage1/$($f)*
    $f
    $inputfiles.Count

    $outputfile = './output-stage2/{0}.csv' -f $f
    rm $outputfile

    if ($inputfiles.Count -eq 0) { continue }

    $header = "Name of Owner", "Address", "Location of Property", "Description of Property", "Value", "Currency Code"
    ($header -join ",") + ",Page Number" | out-File $outputfile -Encoding utf8BOM

    foreach ($pfile in $inputfiles) {
        $pagenum = $pfile.Name.Replace("-table-1", "").Split("-")[-1]
        $c = Get-Content -Path $pfile.FullName -Encoding utf8BOM | 
        Select-Object -Skip 1 | 
        ConvertFrom-Csv -Header $header | 
        Select-Object -Property *, @{Name = 'Pagenum'; Expression = { $pagenum } }
        
        $c | ConvertTo-Csv -UseQuotes AsNeeded | 
        Select-Object -Skip 1 | 
        Out-File $outputfile -Append -Encoding utf8BOM
    }

}
