// Funcion para manejar la transición del carousel
window.addEventListener("load", () => {
  const carrusel = document.querySelector(".carrusel-items");

  // console.log(carrusel.scrollWidth);
  // console.log(carrusel.clientWidth);

  let maxScrollLeft = carrusel.scrollWidth - carrusel.clientWidth;
  let intervalo = null;
  let step = 1;
  const start = () => {
    intervalo = setInterval(function () {
      carrusel.scrollLeft = carrusel.scrollLeft + step;
      if (carrusel.scrollLeft === maxScrollLeft) {
        step = step * -1;
      } else if (carrusel.scrollLeft === 0) {
        step = step * -1;
      }
    }, 10);
  };

  const stop = () => {
    clearInterval(intervalo);
  };

  carrusel.addEventListener("mouseover", () => {
    stop();
  });

  carrusel.addEventListener("mouseout", () => {
    start();
  });

  setTimeout(() => {
    start();
  }, 1500);
});


// Control del deslizamiento del navbar al escrollear hacia arriba.
var lastScrollTop = 0;

window.addEventListener("scroll", function(){  
   var st = window.pageYOffset || document.documentElement.scrollTop;  
   if (st > lastScrollTop){
       document.getElementById("topmenu").style.top = "-100%";
   } else {
      document.getElementById("topmenu").style.top = "0";
   }
   lastScrollTop = st;
}, false);

// Manejo de mensajes con SweetAlert, capturamos el botón, escuchamos el evento click y ejecutamos lo deseado.
let btn_send = document.getElementById("send_message");

btn_send.addEventListener("click", function(){  
  // Validación sencilla
  let name_send = document.getElementById("name_message").value;
  let email_send = document.getElementById("mail_message").value;
  let text_send = document.getElementById("text_message").value;

  if(name_send && email_send && text_send){
    swal({
      title: "Correcto",
      text: "Mensaje enviado correctamente",
      icon: "success",
      button: "Excelente",
    });
  } else{
    swal({
      title: "Error",
      text: "Completa todos los campos",
      icon: "error",
      button: "Correcto",
    });
  }
});
