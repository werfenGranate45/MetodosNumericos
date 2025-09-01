document.getElementById("btnSeno").addEventListener("click", () => {
    //Para java script deja de usar el var xdxd
    const conf = confirm("¿Seguro que quieres ir a la página seno?");

    if(!conf)
       window.location.href = window.location.origin
});

 // Redirección para coseno (ruta absoluta)
document.getElementById("btnCoseno").addEventListener("click", () => {
    //Para java script deja de usar el var xdxd
    let conf = confirm("¿Seguro que quiere calcular el coseno?");

    if(!conf)
       window.location.href = window.location.origin
});

// Redirección para exponencial (con confirmación)
document.getElementById("btnExp").addEventListener("click", () => {
     //Para java script deja de usar el var xdxd
   const conf = confirm("¿Seguro que quiere calcular el exponencial?");
   alert("PEPE")
   if(!conf){
    alert("Hola")
       console.log("Mi verga")
       window.location.href = '/'
   }
       
});


