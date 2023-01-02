function onlyNumberKey(evt) { 
    // Only ASCII charactar in that range allowed 
    var ASCIICode = (evt.which) ? evt.which : evt.keyCode 
    if ((ASCIICode < 43 || ASCIICode > 43) && (ASCIICode < 48 || ASCIICode > 57))
        return false; 
    return true; 
}


