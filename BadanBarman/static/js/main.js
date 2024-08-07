// ! ++++++++++++++++++++++++++++++++++++++++++++++++++++
// * ============ Contain common animation ==============
// ! ++++++++++++++++++++++++++++++++++++++++++++++++++++




// ! ****************************************************
// *** ToggleMenu Berger animation...
// ! ****************************************************


document.addEventListener("DOMContentLoaded",function(){
    document.getElementById("toggleMenuInitial").onclick = function() {myFunctionShow()};
    document.getElementById("toggleMenuFinal").onclick = function() {myFunctionHide()};
    document.getElementById("menu-contact-hide").onclick = function() {myFunctionHide()};
    document.getElementById("menu-publication-hide").onclick = function() {myFunctionHide()};
    
    function myFunctionShow() {
        document.getElementById("showMenu").classList.toggle("translate-y-full");
        document.getElementById("showMenu").classList.toggle("opacity-1");
        document.getElementById("showMenu").classList.remove("-translate-y-full");
        document.getElementById("showMenu").classList.remove("opacity-0");
    }
    
    
    function myFunctionHide() {
        document.getElementById("showMenu").classList.toggle("-translate-y-full");
        document.getElementById("showMenu").classList.remove("translate-y-full");
            document.getElementById("showMenu").classList.remove("opacity-1");
            document.getElementById("showMenu").classList.toggle("opacity-0");
        }
        
    })

// !====================================================================
// *               Page Transition animation...
// !====================================================================
document.addEventListener("DOMContentLoaded",function(){
    document.getElementById("main-body").classList.toggle("opacity-1");
    document.getElementById("main-body").classList.remove("opacity-0");
})
