$(document).ready(function(){
	appenddata = ''
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
            if (output[i]["status"] == 'open'){
              status =  `<span class="badge rounded-pill bg-primary w-100">Open</span>`
            }else if (output[i]["status"] == 'progress'){
              status =  `<span class="badge rounded-pill bg-warning w-100">Progress</span>`
            }
          	appenddata += `<tr>
            <td>PRC - `+output[i]["parcel_id"]+`</td>
            <td>`+output[i]["from_branch"]+`</td>
            <td>`+output[i]["created_at"]+`</td>
            <td>`+status+`</td>`
            +`<td><button class='btn btn-primary' onclick=parceldetail('`+output[i]["parcel_id"]+`')>Check</button></td>`+`
          </tr>`
          }
         
          $("#parceldetails").html(appenddata)
          
        },
        error:function(){
          $(".loader").hide();
          alert("Something went wrong! Please try again.")
        }
	});
});

function parceldetail(parcelid){
  $.ajax({
      url:"/getparceldetail", 
      type: "post", 
      dataType: 'json',
      data: {"parcelid":parcelid},
      success: function(output){
            $(".loader").show();
            $("#spanpresenthub").html(output["city"])
            let mapframe = 'http://maps.google.com/maps?q='+output["lat"]+','+output["lang"]+'&z=16&output=embed'
            $("#mapframe").prop("src", mapframe)
        }
      });
  $("#spanluggageid").html("PRC - "+parcelid)
  let imgurl = 'http://localhost:5000/static/barcodes/lug'+parcelid+'.png'
  $("#qrimage").attr("src",imgurl)
  $("#showMod").click()
  $("#showMod").click()
}