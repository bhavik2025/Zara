// login button click event
    $("#loginSub").click(function () {
        let mail = document.getElementById("userMail").value;
        let pass = document.getElementById("userPass").value;
        let result = eel.checkUser(mail,pass)();
        console.log(result);
        if (result == 1) {
            console.log("in if")
            eel.playAssistantSound();
            eel.speak("Hello Wellcome How Can I Help You...");
            // eel.speak("Error occurred:", error.toString());
            $("#Oval").attr("hidden", false);
            $("#LoginSec").attr("hidden", true);
        }
        else{
            console.log("in else");
            eel.speak("Something is wrong in your Mail or PAssword. Try Again...");
        }
    });