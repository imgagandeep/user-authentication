function check_pass(){
    let new_pass = $("#new-password").val();
    let new_conf_pass = $("#new-conf-password").val();
    
    if(new_pass == new_conf_pass) {
        $("#new-password").css("border","1px solid green");
        $("#new-conf-password").css("border","1px solid green");

        $("#submit_button").removeAttr("disabled");
    }
    else {
        $("#new-password").css("border","1px solid red");
        $("#new-conf-password").css("border","1px solid red");

        $("#submit_button").attr("disabled","disabled");
    }
}



