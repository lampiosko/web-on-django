
$.validator.addMethod("terminaPor",function(value,element,parametro){
  if(value.endsWith(parametro)){
      return true;
  }
  return false;
},"Debe terminar por {0}")



$("#formulario").validate({
  rules: {
      nombre:{
          required:true,
          minlength: 3,
          maxlength: 30
      },
      correo:{
          required:true,
          email:true,
          terminaPor:"@gmail.com"
      },
      tipoSolicitud:{
          required:true
      },
      mensaje:{
          required:true,
          minlength: 3,
          maxlength: 300
      }
  }
})


$("#btnGuardar").click(function() {
  if($("#formulario").val() == false){
      return;
  }
  let nombre = $("#nombre").val()
  let correo =$("#correo").val()
  let tipoSolicitud = $("#tipo_solicitud").val()
  let mensaje = $("#mensaje").val()
  let aviso = $("#avisos").is(":checked")

  console.log(nombre)
})

