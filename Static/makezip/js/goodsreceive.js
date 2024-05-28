$(document).ready(function(){

  $("#luggageid").change(function(){

    var luggageid = $("#luggageid").val()
    $.ajax({
      url:"/getparcelcount", 
      type: "post", 
      dataType: 'json',
      data: {"luggageid":luggageid},
      success: function(output){
        $("#actualno").val(output[0]["total"])
      }
  });
  });

  $.ajax({
      url:"/getopenlug", 
      type: "post", 
      dataType: 'json',
      data: {},
      beforeSend: function(){
            $(".loader").show();
        },
        success: function(output){
          var opt = "<option>Select an option</option>"
          for(var i= 0; i<=output.length - 1;i++){
            opt += "<option value='"+output[i]["luggage_id"]+"'>"+"LUG"+" - "+output[i]["luggage_id"]+"</option>"
          }
          $("#luggageid").append(opt)
        },
        error:function(){
          $(".loader").hide();
          alert("Something went wrong! Please try again.")
        }
    });

  $.ajax({
    url:"/getbranchlist", 
    type: "post", 
    dataType: 'json',
    data: {},
    beforeSend: function(){
          $(".loader").show();
      },
      success: function(output){
        var opt = "<option>Select an option</option>"
        for(var i= 0; i<=output.length - 1;i++){
          opt += "<option value='"+output[i]["branch_id"]+"'>"+output[i]["branch_name"]+"</option>"
        }
        $("#frombranch").append(opt)
        $("#tobranch").append(opt)
      },
      error:function(){
        $(".loader").hide();
        alert("Something went wrong! Please try again.")
      }
  });

  $("#addgr").click(function(){

    var luggageid = $("#luggageid").val()
    var frombranch = $("#frombranch").val()
    var tobranch = $("#tobranch").val()
    var actualno = $("#actualno").val()
    var receivedno = $("#receivedno").val()
    var missed = $("#missed").val()
    var comments = $("#comments").val()

    if (luggageid == '' || frombranch == '' || tobranch == '' || receivedno == '' || actualno == ''){
      $("#info").text("Enter all the mandatory fields")
       $("#info").css("color","red")
        $("#info").show()
    }else{
      $.ajax({
          url:"/addgrnotes", 
          type: "post", 
          dataType: 'json',
          data: {"luggageid":luggageid, "frombranch":frombranch, "tobranch":tobranch, "actualno":actualno, "receivedno":receivedno, "missed":missed, "comments":comments},
          beforeSend: function(){
                $(".loader").show();
            },
            success: function(output){
              $("#info").text("GR Notes added successfully!")
               $("#info").css("color","green")
                $("#info").show()
            },
            error:function(){
              $(".loader").hide();
              alert("Something went wrong! Please try again.")
            }
        });
    }

  });

});

