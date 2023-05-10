# Read all of the unsecuredclaims csv files generated from camelot and combine 
# them into one file for each docket

$filelist = "242-blockfiinc-unsecuredclaims", "247-blockfiintl-unsecuredclaims", "251-lendingllc-unsecuredclaims", "461-lendingllc-unsecuredclaims", "462-blockfiintl-unsecuredclaims"

foreach ($f in $filelist) {
    $inputfiles = Get-ChildItem -Path ./output-stage1/$($f)*
    $f
    $inputfiles.Count

    $outputfile = './output-stage2/{0}.csv' -f $f
    rm $outputfile

    if ($inputfiles.Count -eq 0) { continue }

    $header = "Name of Owner", "Address", "AccountNum", "Debt Date Incurred", "Basis for Claim", "Contigent", "Unliquidated", "Disputed", "offset", "Total Claim"
    ($header -join ",") + ",Page Number" | out-File $outputfile -Encoding utf8BOM

    foreach ($pfile in $inputfiles) {
        $pagenum = $pfile.Name.Replace("-table-1", "").Split("-")[-1]
        $c = Get-Content -Path $pfile.FullName -Encoding utf8BOM | 
        Select-Object -Skip 1  | 
        ConvertFrom-Csv -Header $header | 
        Select-Object -Property *, @{Name = 'Pagenum'; Expression = { $pagenum } }
    
        $c | ConvertTo-Csv -UseQuotes AsNeeded | 
        Select-Object -Skip 1 | 
        Out-File $outputfile -Append -Encoding utf8BOM
    }
}