// Manejo de mensajes con SweetAlert, capturamos el botón, escuchamos el evento click y ejecutamos lo deseado.
let add_doctor = document.getElementById("add_doctorForm");
let add_patient = document.getElementById("add_patientForm");
let add_socialWork = document.getElementById("add_socialWorkForm");
let add_clinic = document.getElementById("add_clinicForm");

// Formulario del Doc
add_doctor?.addEventListener("click", function(){  
  // Validación sencilla
  console.log("asa")
  let nameDoctor = document.getElementById("name-doctor").value;
  let scpecialtyDoctor = document.getElementById("specialty-doctor").value;
  let emailDoctor = document.getElementById("email-doctor").value;
  let campusDoctor = document.getElementById("campus-doctor").value;
  let horaryDoctor = document.getElementById("horary-doctor").value;
  let stateDoctor = document.getElementById("state-doctor").value;

  // Por ahora solo con uno de todos para futuros tests
  // if(nameDoctor && scpecialtyDoctor && emailDoctor && campusDoctor && horaryDoctor && stateDoctor){
  if(nameDoctor){
    swal({
      title: "Correcto",
      text: "Doctor Agregado",
      icon: "success",
      button: "Excelente",
    });
  } else{
    swal({
      title: "Error",
      text: "Completa los campos requeridos",
      icon: "error",
      button: "Correcto",
    });
  }
});

// Formulario de los pacientes
add_patient?.addEventListener("click", function(){  
  // Validación sencilla
  let namePacient = document.getElementById("name-patient").value;
  let socialWorkPacient = document.getElementById("socialWork-patient").value;
  let emailPacient = document.getElementById("email-patient").value;
  let phonePacient = document.getElementById("phone-patient").value;
  let adressPacient = document.getElementById("adress-patient").value;
  let statePacient = document.getElementById("state-patient").value;

  // Por ahora solo con uno de todos para futuros tests
  // if(namePacient && socialWorkPacient && emailPacient && phonePacient && adressPacient && statePacient){
  if(namePacient){
      swal({
      title: "Correcto",
      text: "Paciente Agregado",
      icon: "success",
      button: "Excelente",
    });
  } else{
    swal({
      title: "Error",
      text: "Completa los campos requeridos",
      icon: "error",
      button: "Correcto",
    });
  }
});

// Formulario de las obras sociales
add_socialWork?.addEventListener("click", function(){  
  // Validación sencilla
  let socialWork = document.getElementById("socialWork-form").value;
  let planForm = document.getElementById("plan-form").value;

  // Por ahora solo con uno de todos para futuros tests.
  // if(socialWorkPacient && planForm){
  if(socialWork){
      swal({
      title: "Correcto",
      text: "Obra Social Agregada",
      icon: "success",
      button: "Excelente",
    });
  } else{
    swal({
      title: "Error",
      text: "Completa los campos requeridos",
      icon: "error",
      button: "Correcto",
    });
  }
});

// Formulario de las obras sociales
add_clinic?.addEventListener("click", function(){  
  let nameClinic = document.getElementById("name-clinic").value;
  let scheduleClinic = document.getElementById("schedule-clinic").value;
  let emailClinic = document.getElementById("email-clinic").value;
  let phoneClinic = document.getElementById("phone-clinic").value;
  let campusClinic = document.getElementById("campus-clinic").value;

  // Por ahora solo con uno de todos para futuros tests
  // if(nameClinic && scheduleClinic && emailClinic && phoneClinic && campusClinic){
  if(nameClinic){
      swal({
      title: "Correcto",
      text: "Clínica Agregada",
      icon: "success",
      button: "Excelente",
    });
  } else{
    swal({
      title: "Error",
      text: "Completa los campos requeridos",
      icon: "error",
      button: "Correcto",
    });
  }
});