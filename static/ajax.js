function submitSME(evt) {
    
    evt.preventDefault();

    const formData = {
      lesson_id: $("#lesson_id").val(),
      sme_id: $("#sme-id").val()
    };
    
    $.ajax({
      url: "/updateLessonSme",
      method: "POST",
      data: JSON.stringify(formData),
      contentType: "application/json",
      success: (response) => {
        console.log(response)
        $("#sme_name").text(response)
    },
    });
  }

  
  
  $("#add-sme").on("submit", submitSME);
  