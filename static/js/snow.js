// Snow from https://codepen.io/radum/pen/xICAB

(function () {

    let COUNT = 300;
    let masthead = document.querySelector('.sky');
    let canvas = document.createElement('canvas');
    let ctx = canvas.getContext('2d');
    let width = masthead.clientWidth;
    let height = masthead.clientHeight;
    let i = 0;
    let active = false;

    function onResize() {
      width = masthead.clientWidth;
      height = masthead.clientHeight;
      canvas.width = width;
      canvas.height = height;
      ctx.fillStyle = '#FFF';

      let wasActive = active;
      active = width > 600;

      if (!wasActive && active)
        requestAnimFrame(update);
    }

    let Snowflake = function () {
      this.x = 0;
      this.y = 0;
      this.vy = 0;
      this.vx = 0;
      this.r = 0;

      this.reset();
    }

    Snowflake.prototype.reset = function() {
      this.x = Math.random() * width;
      this.y = Math.random() * -height;
      this.vy = 1 + Math.random() * 3;
      this.vx = 0.5 - Math.random();
      this.r = 1 + Math.random() * 2;
      this.o = 0.5 + Math.random() * 0.5;
    }

    canvas.style.position = 'absolute';
    canvas.style.left = canvas.style.top = '0';

    let snowflakes = [], snowflake;
    for (i = 0; i < COUNT; i++) {
      snowflake = new Snowflake();
      snowflake.reset();
      snowflakes.push(snowflake);
    }

    function update() {

      ctx.clearRect(0, 0, width, height);

      if (!active)
        return;

      for (i = 0; i < COUNT; i++) {
        snowflake = snowflakes[i];
        snowflake.y += snowflake.vy;
        snowflake.x += snowflake.vx;

        ctx.globalAlpha = snowflake.o;
        ctx.beginPath();
        ctx.arc(snowflake.x, snowflake.y, snowflake.r, 0, Math.PI * 2, false);
        ctx.closePath();
        ctx.fill();

        if (snowflake.y > height) {
          snowflake.reset();
        }
      }

      requestAnimFrame(update);
    }

    // shim layer with setTimeout fallback
    window.requestAnimFrame = (function(){
      return  window.requestAnimationFrame       ||
              window.webkitRequestAnimationFrame ||
              window.mozRequestAnimationFrame    ||
              function( callback ){
                window.setTimeout(callback, 1000 / 60);
              };
    })();

    onResize();
    window.addEventListener('resize', onResize, false);

    masthead.appendChild(canvas);
  })();

// Get the element
let colorElement = document.querySelector('.color:nth-child(1)');

// Define the colors
let colors = ['#FF6C6C', '#FF3737'];

// Define the duration of each color
let duration = 5000; // 5 seconds

// Define the current color index
let currentIndex = 0;

// Function to change the color
function changeColor() {
    // Set the background color
    colorElement.style.background = colors[currentIndex];

    // Increment the current color index
    currentIndex = (currentIndex + 1) % colors.length;

    // Call the function again after the duration
    setTimeout(changeColor, duration);
}

// Call the function for the first time
changeColor();