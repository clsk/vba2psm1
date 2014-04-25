
    $excel = new-object -comobject Excel.Application
    $excel.Visible = $true
    $Workbook = $excel.workbooks.Add()
    $Worksheets = $excel.Worksheets

    function Sheets($id) {
        return $Worksheets.Item($id)
    }

    function Workbooks {
        return $excel.Worksheet
    }

    function Range() {
        return $excel.Range
    }

Export-ModuleMember -Function Load-EVBA
Export-ModuleMember -Function Sheets
Export-ModuleMember -Function Workbooks
Export-ModuleMember -Function Range
Export-ModuleMember -Variable $excel
Export-ModuleMember -Variable $Workbook
Export-ModuleMember -Variable $Worksheets

