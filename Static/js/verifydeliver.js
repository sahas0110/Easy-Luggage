$(document).ready(function(){
  
appenddata = '<option value="">Select the luggage to be delivered</option>'
	$.ajax({
      url:"/getallparcels", 
      type: "post", 
      dataType: 'json',
      data: {},
      beforeSend: function(){
            $(".loader").show();
        },
        success: function(output){
          for(var i=0; i<= output.length-1; i++){
            if (output[i]["status"] == 'open' || output[i]["status"] == 'progress'){
              appenddata += '<option value="'+output[i]["parcel_id"]+'">PRC - '+output[i]["parcel_id"]+'</option>'
            }
          }
          $("#parcelid").append(appenddata)
        },
        error:function(){
          $(".loader").hide();
          alert("Something went wrong! Please try again.")
        }
	});


  $("#getdetails").click(function(){
     let parcelid = $("#parcelid").val()
    $.ajax({
        url:"/getparcelcompdetail", 
        type: "post", 
        dataType: 'json',
        data: {"parcelid":parcelid},
        beforeSend: function(){
            $(".loader").show();
        },
        success: function(output){
          $("#spanluggageid").html("LUG - "+output["parcel"][0]["luggage_id"])
          $("#curlugid").val(output["parcel"][0]["parcel_id"])
          $("#spanparcelid").html("PRC - "+output["parcel"][0]["parcel_id"])
          $("#spanusername").html(output["userdetail"][0]["user_name"])
          $("#spanphone").html(output["userdetail"][0]["phone"])
          $("#spanaddress").html(output["userdetail"][0]["address"])
          $("#activity").show()
        },
        error:function(){
          $(".loader").hide();
          alert("Something went wrong! Please try again.")
        }
  });
  });

  $("#verifyuser").click(function(){
    let parcelid = $("#parcelid").val()
    $.ajax({
        url:"/verifyuser", 
        type: "post", 
        dataType: 'json',
        data: {"parcelid":parcelid},
        success: function(output){
          if (output == 'yes'){
            var op = '<span class="badge bg-success"><i class="bi bi-check-circle me-1"></i> Verified Successfully!</span>'
            $("#deliveruser").show();
          }else{
            var op = '<span class="badge bg-danger"><i class="bi bi-exclamation-octagon me-1"></i> Credentials Not Matching!</span>'
            $("#deliveruser").hide();
          }
          $("#resultfield").html(op)
        },
        error:function(){
          $(".loader").hide();
          alert("Something went wrong! Please try again.")
        }
      });
    
  });

  $("#deliveruser").click(function(){
    let curlugid = $("#curlugid").val()
    $.ajax({
        url:"/deliveruser", 
        type: "post", 
        dataType: 'json',
        data: {"curlugid":curlugid},
        success: function(output){
          if (output == '1'){
            $("#deliveruser").text("Delivered Successfully!");
            $("#deliveruser").attr("disabled", true)
          }else{
            $("#deliveruser").hide();
          }
          
        },
        error:function(){
          $(".loader").hide();
          alert("Something went wrong! Please try again.")
        }
      });
  })

});
