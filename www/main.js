function loadCSSFile(filename) {
    const link = document.createElement('link');
    link.rel = 'stylesheet';
    link.type = 'text/css';
    link.href = filename; // Path to the CSS file
    document.head.appendChild(link);
}

$(document).ready(function () {

    eel.init()()

    $('.text').textillate({
        loop: true,
        sync: true,
        in: {
            effect: "bounceIn",
        },
        out: {
            effect: "bounceOut",
        },
    });

    // Siri Configuration

    var siriWave = new SiriWave({
        container: document.getElementById("siri-container"),
        width: 940,
        height: 200,
        style: "ios9",
        amplitude: "1.5",
        frequency: "20",
        speed: ".30",
        autostart: true
    });
    // siri message animation
    $('.siri-message').textillate({
        loop: true,
        sync: true,
        in: {
            effect: "pulse",
            sync: true,
        },
        out: {
            effect: "pulse",
            sync: true,
        },
    });

    // login button click event
    $("#loginSub").click(async function (event) {
        event.preventDefault(); 
        let mail = document.getElementById("userMail").value;
        let pass = document.getElementById("userPass").value;
        let result = await eel.checkUser(mail,pass)();
        if (result == 1) {
            dynamicDisplay();
            eel.playAssistantSound();
            $("#Oval").attr("hidden", false);
            $("#LoginSec").attr("hidden", true);
        }
        else{
            eel.speak("Something is wrong in your Mail or PAssword. Try Again...");
        }
    });

    // signup button click event
    $("#signupbtn").click(async function (event) {
        event.preventDefault(); 
        let name = document.getElementById("sigeupname").value;
        let pass = document.getElementById("signupPass").value;
        let mail = document.getElementById("sigeupmail").value;
        let mo= document.getElementById("signupmo").value;
        if(name=="" || pass=="" || mail=="" || mo=="")
        {
            eel.speak("You have to fill the form...");
        }
        else
        {
            await eel.userinsert(name, pass, mail, mo)(); // Execute eel function
            $("#signinSec").attr("hidden", true);
            $("#LoginSec").attr("hidden", false);
        }
    });

    // Mic button click event
    $("#MicBtn").click(function () {
        eel.playAssistantSound();
        $("#Oval").attr("hidden", true);
        $("#SiriWave").attr("hidden", false);
        eel.allCommands()()
    });

    // personal button click event
    $("#Personal").click(function () {
        $("#personalDetail").attr("hidden", false);
        $("#setCommand").attr("hidden", true);
        $("#setContact").attr("hidden", true);
        $("#setMemory").attr("hidden", true);
    });
    
    // Edit Button Clicked
    $("#Edit").click(function () {
        $("#PD_Edit").attr("hidden", false);
    });
    
    // Update Data
    $("#updatePD").click(function () {
        const ename = document.getElementById('PName').value;
        const email = document.getElementById('PMail').value;
        const epass = document.getElementById('PPass').value;
        const emo = document.getElementById('PMobile').value;
        console.log(ename);
        console.log(email);
        console.log(epass);
        console.log(emo);
        eel.updatePD(ename,epass,email,emo);
        dynamicDisplay();
        $("#PD_Edit").attr("hidden", true);
    });
    
    // Delete Profile
    $("#Delete").click(function () {
        eel.DeletePD();
    });

    // command button click event
    $("#Command").click(function () {
        $("#personalDetail").attr("hidden", true);
        $("#setCommand").attr("hidden", false);
        $("#setContact").attr("hidden", true);
        $("#setMemory").attr("hidden", true);
    });

    // Phone Book button click event
    $("#Phone").click(function () {
        $("#personalDetail").attr("hidden", true);
        $("#setCommand").attr("hidden", true);
        $("#setContact").attr("hidden", false);
        $("#setMemory").attr("hidden", true);
    });

    // Memory button click event
    $("#Memory").click(function () {
        $("#personalDetail").attr("hidden", true);
        $("#setCommand").attr("hidden", true);
        $("#setContact").attr("hidden", true);
        $("#setMemory").attr("hidden", false);
    });

    // System button click event
    $("#setSystem").click(function () {
        $("#System").attr("hidden", false);
        $("#Web").attr("hidden", true);
        let webcolor = document.getElementById("Web").style.color
        console.log();
    });

    // Web button click event
    $("#setWeb").click(function () {
        $("#System").attr("hidden", true);
        $("#Web").attr("hidden", false);
        $("#System").attr("color", blue);
        $("#Web").attr("color", white);
    });

    function doc_keyUp(e) {
        // this would test for whichever key is 40 (down arrow) and the ctrl key at the same time
        if (e.key === 'z' && e.altKey) {
            eel.playAssistantSound()
            $("#Oval").attr("hidden", true);
            $("#SiriWave").attr("hidden", false);
            eel.allCommands()()
        }
    }
    document.addEventListener('keyup', doc_keyUp, false);

    // to play assisatnt 
    function PlayAssistant(message) {
        if (message != "") {
            $("#Oval").attr("hidden", true);
            $("#SiriWave").attr("hidden", false);
            eel.allCommands(message);
            $("#chatbox").val("")
            $("#MicBtn").attr('hidden', false);
            $("#SendBtn").attr('hidden', true);
        }
    }

    // toogle fucntion to hide and display mic and send button 
    function ShowHideButton(message) {
        if (message.length == 0) {
            $("#MicBtn").attr('hidden', false);
            $("#SendBtn").attr('hidden', true);
        }
        else {
            $("#MicBtn").attr('hidden', true);
            $("#SendBtn").attr('hidden', false);
        }
    }

    // key up event handler on text box
    $("#chatbox").keyup(function () {

        let message = $("#chatbox").val();
        ShowHideButton(message)

    });

    // settings button click event
    $("#SettingsBtn").click(function () {

    });

    // send button event handler
    $("#SendBtn").click(function () {

        let message = $("#chatbox").val()
        PlayAssistant(message)

    });

    // enter press event handler on chat box
    $("#chatbox").keypress(function (e) {
        key = e.which;
        if (key == 13) {
            let message = $("#chatbox").val()
            PlayAssistant(message)
        }
    });

});


// -----------------------------------------------------------------display data start -------------------------------------------------------------------------------

// Function to dynamically load and display data
async function dynamicDisplay() {
    try {
        // Fetch data from Python backend
        const SysData = await eel.displaySysCommand()();
        const webData = await eel.displayWebCommand()();
        const contactData = await eel.displayContact()();
        const memoryData = await eel.displayMemory()();
        const personalData = await eel.displayPersonalDetails()();

        // Get table body elements
        const sysBody = document.getElementById('sys-body');
        const webBody = document.getElementById('web-body');
        const contactBody = document.getElementById('contact-body');
        const memoryBody = document.getElementById('memory-body');
        
        // Personal Details Components
        const name = document.getElementById('Name');
        const mail = document.getElementById('Mail');
        const pass = document.getElementById('Pass');
        const mo = document.getElementById('Mo');

        personalData.forEach(item => {
            let nameData = item[1];
            let mailData = item[2];
            let passData = item[3];
            let moData = item[4];

            name.innerHTML = nameData;
            mail.innerHTML = mailData;
            pass.innerHTML = passData;
            mo.innerHTML = moData;

        });

        // Clear existing table rows
        sysBody.innerHTML = "";
        webBody.innerHTML = "";
        contactBody.innerHTML = "";
        memoryBody.innerHTML = "";

        // Dynamically populate rows
        let sysno = 1;
        SysData.forEach(item => {
            const row = `<tr>
                <td>${sysno}</td>
                <td>${item[1]}</td>
                <td>${item[2]}</td>
                <td><button class="dlt_Btn sysDlt" id="${item[0]}">Delete</button></td>
            </tr>`;
            sysno++;
            sysBody.innerHTML += row;
        });

        let webno = 1;
        webData.forEach(item => {
            const row = `<tr>
                <td>${webno}</td>
                <td>${item[1]}</td>
                <td>${item[2]}</td>
                <td><button class="dlt_Btn webDlt" id="${item[0]}">Delete</button></td>
            </tr>`;
            webno++;
            webBody.innerHTML += row;
        });

        let contactno = 1;
        contactData.forEach(item => {
            const row = `<tr>
                <td>${contactno}</td>
                <td>${item[1]}</td>
                <td>${item[2]}</td>
                <td><button class="dlt_Btn contactDlt" id="${item[0]}">Delete</button></td>
            </tr>`;
            contactno++;
            contactBody.innerHTML += row;
        });

        let memoryno = 1;
        memoryData.forEach(item => {
            const row = `<tr>
                <td>${memoryno}</td>
                <td>${item[1]}</td>
                <td><button class="dlt_Btn memoryDlt" id="${item[0]}">Delete</button></td>
            </tr>`;
            memoryno++;
            memoryBody.innerHTML += row;
        });
    } catch (error) {
        eel.speak("Error occurred:", error.toString());
    }
}

// Initial data loading on DOMContentLoaded
document.addEventListener("DOMContentLoaded", dynamicDisplay);

// Event listener for delete buttons
document.addEventListener("click", async function (event) {
    if (event.target && event.target.classList.contains("sysDlt")) {
        event.preventDefault();
        const id = event.target.id;
        await eel.deleteSystem(id); // Call Python function
        await dynamicDisplay();    // Refresh data
    }
    if (event.target && event.target.classList.contains("webDlt")) {
        event.preventDefault();
        const id = event.target.id;
        await eel.deleteWeb(id);
        await dynamicDisplay();
    }
    if (event.target && event.target.classList.contains("contactDlt")) {
        event.preventDefault();
        const id = event.target.id;
        await eel.deleteContact(id);
        await dynamicDisplay();
    }
    if (event.target && event.target.classList.contains("memoryDlt")) {
        event.preventDefault();
        const id = event.target.id;
        await eel.deleteMemory(id);
        await dynamicDisplay();
    }
});
// Event listener for adding new data
document.addEventListener("click", async function (event) {
    event.preventDefault(); // Prevent any default behavior

    if (event.target && event.target.classList.contains("addSys")) {
        const key = document.getElementById("sysKeyword").value;
        const path = document.getElementById("sysPath").value;
        if (key && path) {
            await eel.insertSys(key, path)(); // Add data
            document.getElementById("sysKeyword").value = "";
            document.getElementById("sysPath").value = "";
            await dynamicDisplay();          // Refresh data
        }
        
    }

    if (event.target && event.target.classList.contains("addWeb")) {
        const key = document.getElementById("webKeyword").value;
        const path = document.getElementById("webPath").value;

        if (key && path) {
            await eel.insertWeb(key, path)();
            document.getElementById("webKeyword").value = "";
            document.getElementById("webPath").value = "";
            await dynamicDisplay();
        }
    }

    if (event.target && event.target.classList.contains("addContact")) {
        const name = document.getElementById("contactName").value;
        const no = document.getElementById("contactNo").value;

        if (name && no) {
            await eel.insertConatct(name, no)();
            document.getElementById("contactName").value = "";
            document.getElementById("contactNo").value = "";
            await dynamicDisplay();
        }
    }
});