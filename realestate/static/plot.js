const images1 = [
    'static/PLOT1.JPG.jpeg',
    'static/PLOT2.JPG.jpeg',
    'static/PLOT3.JPG.jpeg',
    'static/PLOT4.JPG.jpeg',
    'static/PLOT5.JPG.jpeg',
];
var currentIndex1 = 0;
const slideshowImage1 = document.getElementById('slideshow-image1');
const prevButton1 = document.getElementById('prev-button1');
const nextButton1 = document.getElementById('next-button1');
function update1() {
    slideshowImage1.src = images1[currentIndex1];
}
if(nextButton1){
    nextButton1.addEventListener('click', () => {
    currentIndex1 = (currentIndex1 + 1) % images1.length; // Loop back to the last image
    update1();
    });
}
if(prevButton1){
    prevButton1.addEventListener('click', () => {
    currentIndex1 = (currentIndex1 - 1 + images1.length) % images1.length; // Loop back to the last image
    update1();
    });
}





const images2 = [
    'static/PLOT2.JPG.jpeg',
    'static/PLOT3.JPG.jpeg',
    'static/PLOT1.JPG.jpeg',
    'static/PLOT4.JPG.jpeg',
    'static/PLOT5.JPG.jpeg',
];
var currentIndex2 = 0;
const slideshowImage2 = document.getElementById('slideshow-image2');
const prevButton2 = document.getElementById('prev-button2');
const nextButton2 = document.getElementById('next-button2');
function update2() {
    slideshowImage2.src = images2[currentIndex2];
}
if(nextButton2){
    nextButton2.addEventListener('click', () => {
    currentIndex2 = (currentIndex2+ 1) % images2.length; // Loop back to the last image
    update2();
    });
}
if(prevButton2){
    prevButton2.addEventListener('click', () => {
    currentIndex2 = (currentIndex2 - 1 + images2.length) % images2.length; // Loop back to the last image
    update2();
    });
}   




const images3 = [
    'static/PLOT3.JPG.jpeg',
    'static/PLOT1.JPG.jpeg',
    'static/PLOT4.JPG.jpeg',
    'static/PLOT2.JPG.jpeg',
    'static/PLOT5.JPG.jpeg',
];
var currentIndex3 = 0;
const slideshowImage3 = document.getElementById('slideshow-image3');
const prevButton3 = document.getElementById('prev-button3');
const nextButton3 = document.getElementById('next-button3');
function update3() {
    slideshowImage3.src = images3[currentIndex3];
}
if(nextButton3){
    nextButton3.addEventListener('click', () => {
    currentIndex3 = (currentIndex3+ 1) % images3.length; // Loop back to the last image
    update3();
    });
}
if(prevButton3){
    prevButton3.addEventListener('click', () => {
    currentIndex3 = (currentIndex3 - 1 + images3.length) % images3.length; // Loop back to the last image
    update3();
    });
}   





const images4 = [
    'static/PLOT4.JPG.jpeg',
    'static/PLOT2.JPG.jpeg',
    'static/PLOT1.JPG.jpeg',
    'static/PLOT3.JPG.jpeg',
    'static/PLOT5.JPG.jpeg',
];
var currentIndex4 = 0;
const slideshowImage4 = document.getElementById('slideshow-image4');
const prevButton4 = document.getElementById('prev-button4');
const nextButton4 = document.getElementById('next-button4');
function update4() {
    slideshowImage4.src = images4[currentIndex4];
}
if(nextButton4){
    nextButton4.addEventListener('click', () => {
    currentIndex4 = (currentIndex4+ 1) % images4.length; // Loop back to the last image
    update4();
    });
}
if(prevButton4){
    prevButton4.addEventListener('click', () => {
    currentIndex4 = (currentIndex4 - 1 + images4.length) % images4.length; // Loop back to the last image
    update4();
    });
}   





const images5 = [
    'static/PLOT5.JPG.jpeg',
    'static/PLOT3.JPG.jpeg',
    'static/PLOT1.JPG.jpeg',
    'static/PLOT4.JPG.jpeg',
    'static/PLOT2.JPG.jpeg',
];
var currentIndex5 = 0;
const slideshowImage5 = document.getElementById('slideshow-image5');
const prevButton5 = document.getElementById('prev-button5');
const nextButton5 = document.getElementById('next-button5');
function update5() {
    slideshowImage5.src = images5[currentIndex5];
}
if(nextButton5){
    nextButton5.addEventListener('click', () => {
    currentIndex5 = (currentIndex5+ 1) % images5.length; // Loop back to the last image
    update5();
    });
}
if(prevButton5){
    prevButton5.addEventListener('click', () => {
    currentIndex5 = (currentIndex5 - 1 + images5.length) % images5.length; // Loop back to the last image
    update5();
    });
}   





