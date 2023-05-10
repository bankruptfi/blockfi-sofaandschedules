# Read all of the 90 day payment csv files generated from camelot and combine 
# them into one file for each docket

$filelist = "243-blockfiinc-90daypayments", "248-blockfiintl-90daypayments", "252-lendingllc-90daypayments", "256-servicesinc-90daypayments", "262-walletllc-90daypayments"

foreach ($f in $filelist) {
    $inputfiles = Get-ChildItem -Path ./output-stage1/$($f)*
    $f
    $inputfiles.Count

    $outputfile = './output-stage2/{0}.csv' -f $f
    rm $outputfile

    if ($inputfiles.Count -eq 0) { continue }

    #$header = "Name of Owner", "Address", "AccountNum", "Debt Date Incurred", "Basis for Claim", "Contigent", "Unliquidated", "Disputed", "offset", "Total Claim"
    $header = "Creditor Name", "Reasons for payment or transfer", "Dates of Payments", "Total", "Address"
    ($header -join ",") + ",Page Number" | out-File $outputfile -Encoding utf8BOM

    foreach ($pfile in $inputfiles) {
        #$pagenum = 9999
        $pagenum = $pfile.Name.Replace("-table-1", "").Split("-")[-1]
        #if ($pagenum -eq "3") {ls -l $pfile.Name}
        $c = Get-Content -Path $pfile.FullName -Encoding utf8BOM | 
        Select-Object -Skip 1  | 
        ConvertFrom-Csv -Header $header | 
        Select-Object -Property $header[0], $header[1], $header[2], @{Name = 'Total'; Expression = { $_.Total.replace(' ', '') } }, $header[4], @{Name = 'Pagenum'; Expression = { $pagenum } }
    
        $c | ConvertTo-Csv -UseQuotes AsNeeded | 
        Select-Object -Skip 1 | 
        Out-File $outputfile -Append -Encoding utf8BOM
    }
}