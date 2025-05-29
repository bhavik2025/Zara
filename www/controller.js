// $(document).ready(function () {
//     eel.init()()
//     // Display Speak Message
//     eel.expose(DisplayMessage)
//     function DisplayMessage(message) {
//         $(".siri-message").text(message);
//         $('.siri-message').textillate('start');
//     }

//     // Display hood
//     eel.expose(ShowHood)
//     function ShowHood() {
//         $("#Oval").attr("hidden", false);
//         $("#Siriwave").attr("hidden", true);
//     }

//     eel.expose(senderText)
//     function senderText(message) {
//         var chatBox = document.getElementById("chat-canvas-body");
//         if (message.trim() !== "") {
//             chatBox.innerHTML += `<div class="row justify-content-end mb-4">
//             <div class = "width-size">
//             <div class="sender_message">${message}</div>
//         </div>`;

//             // Scroll to the bottom of the chat box
//             chatBox.scrollTop = chatBox.scrollHeight;
//         }
//     }

//     eel.expose(receiverText)
//     function receiverText(message) {

//         var chatBox = document.getElementById("chat-canvas-body");
//         if (message.trim() !== "") {
//             chatBox.innerHTML += `<div class="row justify-content-start mb-4">
//             <div class = "width-size">
//             <div class="receiver_message">${message}</div>
//             </div>
//         </div>`;

//             // Scroll to the bottom of the chat box
//             chatBox.scrollTop = chatBox.scrollHeight;
//         }

//     }

//     // // Hide Loader and display Face Auth animation
//     // eel.expose(hideLoader)
//     // function hideLoader() {

//     //     $("#Loader").attr("hidden", true);
//     //     $("#FaceAuth").attr("hidden", false);

//     // }
//     // // Hide Face auth and display Face Auth success animation
//     // eel.expose(hideFaceAuth)
//     // function hideFaceAuth() {

//     //     $("#FaceAuth").attr("hidden", true);
//     //     $("#FaceAuthSuccess").attr("hidden", false);

//     // }
//     // // Hide success and display 
//     // eel.expose(hideFaceAuthSuccess)
//     // function hideFaceAuthSuccess() {

//     //     $("#FaceAuthSuccess").attr("hidden", true);
//     //     $("#HelloGreet").attr("hidden", false);

//     // }

//     // Hide Start Page and display blob
//     eel.expose(hideStart);
//     async function hideStart() {
//         $("#Start").attr("hidden", true);

//         let first = await eel.signupUser()(); // Ensure asynchronous call
//         console.log("SignupUser response:", first);

//         if (first == 1) {
//             setTimeout(function () {
//                 $("#LoginSec").addClass("animate__animated animate__zoomIn");
//             }, 1000);
//             setTimeout(function () {
//                 $("#LoginSec").attr("hidden", false);
//             }, 1000);
//         } else {
//             setTimeout(function () {
//                 $("#signinSec").addClass("animate__animated animate__zoomIn");
//             }, 1000);
//             setTimeout(function () {
//                 $("#signinSec").attr("hidden", false);
//             }, 1000);
//         }
//     }
// });































































$(document).ready(function () {
    eel.init()();

    // Display Speak Message
    eel.expose(DisplayMessage);
    function DisplayMessage(message) {
        $(".siri-message").text(message);
        $(".siri-message").textillate("start");
    }

    // Show Loader
    eel.expose(ShowHood);
    function ShowHood() {
        $("#Oval").attr("hidden", false);
        $("#Siriwave").attr("hidden", true);
    }

    // Sender and Receiver Text
    eel.expose(senderText);
    function senderText(message) {
        let chatBox = document.getElementById("chat-canvas-body");
        if (message.trim() !== "") {
            chatBox.innerHTML += `<div class="row justify-content-end mb-4">
                <div class="width-size">
                    <div class="sender_message">${message}</div>
                </div>
            </div>`;
            chatBox.scrollTop = chatBox.scrollHeight;
        }
    }

    eel.expose(receiverText);
    function receiverText(message) {
        let chatBox = document.getElementById("chat-canvas-body");
        if (message.trim() !== "") {
            chatBox.innerHTML += `<div class="row justify-content-start mb-4">
                <div class="width-size">
                    <div class="receiver_message">${message}</div>
                </div>
            </div>`;
            chatBox.scrollTop = chatBox.scrollHeight;
        }
    }

    // Hide Start Page
    eel.expose(hideStart);
    function hideStart(res) {
        $("#Start").attr("hidden", true);
        try {
            console.log("Signu response:", res);

            if (res === 1) {
                setTimeout(function () {
                    $("#LoginSec").addClass("animate__animated animate__zoomIn");
                    $("#LoginSec").attr("hidden", false);
                }, 1000);
            } else {
                setTimeout(function () {
                    $("#signinSec").addClass("animate__animated animate__zoomIn");
                    $("#signinSec").attr("hidden", false);
                }, 1000);
            }
        } catch (error) {
            console.error("Error in hideStart:", error);
        }
    }
});
