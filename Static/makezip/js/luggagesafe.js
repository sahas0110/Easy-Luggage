$(document).ready(function(){
	appenddata = ''
	
  $.ajax({
      url:"/getopenlug", 
      type: "post", 
      dataType: 'json',
      data: {},
      beforeSend: function(){
            $(".loader").show();
        },
        success: function(output){
          for(var i=0; i<= output.length-1; i++){
            if (output[i]["status"] == 'open'){
              status =  `<span class="badge rounded-pill bg-primary">Open</span>`
            }else if (output[i]["status"] == 'progress'){
              status =  `<span class="badge rounded-pill bg-warning">Progress</span>`
            }else{
              status =  `<span class="badge rounded-pill bg-success">Delivered</span>`
            }
          	appenddata += `<tr>
            <td>LUG - `+output[i]["luggage_id"]+`</td>
            <td>`+output[i]["from_branch"]+`</td>
            <td>`+output[i]["to_branch"]+`</td>
            <td>`+output[i]["present_hub"]+`</td>
            <td>`+status+`</td>
            <td style='text-align:center'>`+`<i class='bi bi-crosshair2' onclick='tracklug(`+output[i]["luggage_id"]+`)'></i>`+`</td>
          </tr>`
          }
         
          $("#luggagedetails").html(appenddata)
          
        },
        error:function(){
          $(".loader").hide();
          alert("Something went wrong! Please try again.")
        }
	});
  
});

function tracklug(luggageid){

   $.ajax({
      url:"/track", 
      type: "post", 
      dataType: 'json',
      data: {"luggageid":luggageid},
      beforeSend: function(){
            $(".loader").show();
        },
        success: function(output){
          if (output["isright"] == "True"){
            var pt = `<span class="badge rounded-pill bg-primary">Luggage on correct rout</span>`
          }else{
            var pt =  `<span class="badge rounded-pill bg-danger">Luggage not in correct rout</span>`
          }
          $("#pathtrack").html(pt)
          $("#spanpresenthub").html(output["curcity"])
          $("#spanactualhub").html(output["actualcities"])
          $("#showMod").click()
        }
      }
      );


}