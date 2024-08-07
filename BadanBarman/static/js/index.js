console.log("gsap is running")
//* Gsap  ..... 
//* Gsap amimation  ..... 
//* Gsap amimation goes  ..... 
//* Gsap amimation goes here ..... 
// gsap.registerPlugin(ScrollTrigger) 

// ! ****************************************************
// *** Scroll Trigger animation...
// ! ****************************************************
// document.addEventListener("DOMContentLoaded",function(){
//     gsap.to("#second-section",{
//             scrollTrigger:{
//                 trigger: "#second-section",
//                 start: 'top 80%',
//                 toggleActions: "play none none reverse"
//             }, opacity: 1, duration: 1.5
//         })
// })


// ! ****************************************************
// *** Hero-Section animation...
// ! ****************************************************

document.addEventListener("DOMContentLoaded",function(){
    const text = new SplitType('#hero-text')
    gsap.fromTo(".char",{
        y:300,
    },{
        y: 0,
        stagger: 0.1,
        delay: 0.03,
        duration: 1,
        ease: 'power3.out'
    })

    gsap.to(".below-hero-text",{
        opacity: 1,
        delay: 1,
        ease: 'power3.out',
        duration: 0.5,
        stagger: 0.5
    })

    gsap.fromTo(".below-hero-button",{
        y:40,
    },{
        opacity: 1,
        delay: 1.5,
        y:0,
        ease: 'power3.out',
        duration: 1,
    })

    gsap.fromTo("#hero-image",{
        opacity:0,
        rotation: -25,
    },{
        opacity: 1,
        rotation: 6,
        ease: 'power3.out',
        duration: 3,
    })

    gsap.fromTo("#hero-image-div-bg",{
        opacity:0,
        rotation: 0,
    },{
        opacity: 1,
        rotation: -25,
        ease: 'power3.out',
        duration: 3,
    })
})

// ! ****************************************************
// *** Hero-Balls animation...
// ! ****************************************************

document.addEventListener("DOMContentLoaded", function() {
  
    gsap.to("#ball-1", { 
        duration: 3, 
        x: 100 , 
        y: 50, 
        repeat: -1,  
        yoyo: true, 
        ease: 'sine.inOut', }); // Example animation
    gsap.to("#ball-2", { 
        duration: 3, 
        x: -50 , 
        y: 0, 
        repeat: -1,  
        yoyo: true, 
        ease: 'sine.inOut', }); // Example animation
    gsap.to("#ball-3", { 
        duration: 3, 
        x: 75 , 
        y: -50, 
        repeat: -1,  
        yoyo: true, 
        ease: 'sine.inOut', }); // Example animation
    gsap.to("#image-writing-prop",{ 
        duration: 3,
        rotation: 10,
        y: 5,
        repeat: -1,
        yoyo: true,
        ease: 'sine.inOut',
        }) // ! Animation of the writing hand...
    gsap.to("#image-book-prop",{ 
        duration: 2,
        rotationY : 10,
        rotateX: -5,
        scale: 1.035,
        y: 5,
        repeat: -1,
        yoyo: true,
        ease: 'sine.inOut',
        }) // ! Animation of the writing hand...
    gsap.fromTo("#image-prize-prop",{ 
        rotate: -6,
        },{
        duration: 3,
        rotation: 6,
        y: 6,
        repeat: -1,
        yoyo: true,
        ease: 'sine.inOut',
        }) // ! Animation of the writing hand...
    gsap.to("#chat-bot-prop",{ 
        duration: 2,
        y: 5,
        repeat: -1,
        yoyo: true,
        ease: 'sine.inOut',
        }) // ! Animation of the writing hand...
});
