$(document).ready(function(){
	appenddata = ''
	$.ajax({
      url:"/getempdetails", 
      type: "post", 
      dataType: 'json',
      data: {},
      beforeSend: function(){
            $(".loader").show();
        },
        success: function(output){
          for(var i=0; i<= output.length-1; i++){
          	appenddata += `<tr>
            <td>EMP - `+output[i]["serviceman_id"]+`</td>
            <td>`+output[i]["serviceman_name"]+`</td>
            <td>`+output[i]["phone"]+`</td>
            <td>`+output[i]["email"]+`</td>
            <td>`+output[i]["address"]+`</td>
          </tr>`
          }
         
          $("#empdetails").html(appenddata)
          
        },
        error:function(){
          $(".loader").hide();
          alert("Something went wrong! Please try again.")
        }
	});
});