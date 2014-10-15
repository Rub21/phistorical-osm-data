

<%@page contentType="text/html" pageEncoding="UTF-8"%>
<!DOCTYPE html><html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>Convert</title>
    </head>
    <body>
        <script src="http://code.jquery.com/jquery-2.1.0.min.js"></script>
        <script src="http://twbs.github.io/bootstrap/dist/js/bootstrap.min.js"></script>
        <link rel="stylesheet" type="text/css" href="http://twbs.github.io/bootstrap/dist/css/bootstrap.min.css">


        <div class="row">
            <div class="col-md-4"></div>
            <div class="col-md-4">

                <label>Ingresar Geojson :</label>
               

                <textarea id="url" class="form-control" rows="3"  style="height: 200px"></textarea>

                <br>

                <button type="submit" id="button" class="btn btn-default">Submit</button>
                <br>


                <label>Stitch :</label>



                <textarea id="stitch" class="form-control" rows="3"></textarea>
                <br>


                <label>Tilemill :</label>



                <textarea id="tilemill" class="form-control" rows="3"></textarea>
                <br>



                <a id="overpass" >Descargar Overpass</a>





            </div>
            <div class="col-md-4"></div>
        </div>

        <script>

            $(document).on('ready', function() {

                $('#button').click(function() {
                    var obj = JSON.parse($('#url').val());


                    console.log(obj.features[0].geometry.coordinates[2]);

                    var url = [];
                    url[0] = obj.features[0].geometry.coordinates[0][0][0];
                    url[1] = obj.features[0].geometry.coordinates[0][0][1];
                    url[2] = obj.features[0].geometry.coordinates[0][2][0];
                    url[3] = obj.features[0].geometry.coordinates[0][1][1];



                    //http://www.overpass-api.de/api/xapi?map?bbox=-122.51884,37.705317,-122.35302,37.819312
                    //["-122.51884", "37.705317", "-122.35302", "37.819312"]
                    // var stitch = "./stitch -o sf.png -- " + url[1] + " " + url[0] + " " + url[3] + " " + url[2] + " 13 http://a.tiles.mapbox.com/v3/openstreetmap.map-4wvf9l0l/{z}/{x}/{y}.png";
                    var stitch = "./stitch -o file.png -- " + url[1] + " " + url[0] + " " + url[3] + " " + url[2] + " 13 http://a.tiles.mapbox.com/v4/openstreetmap.map-inh7ifmo/{z}/{x}/{y}.png?access_token=pk.eyJ1Ijoib3BlbnN0cmVldG1hcCIsImEiOiJhNVlHd29ZIn0.ti6wATGDWOmCnCYen-Ip7Q";
                    $('#stitch').val(stitch);


                    var tilemill = url[0] + ", " + url[1] + ", " + url[2] + ", " + url[3];
                    $('#tilemill').val(tilemill);

                    var overpass = "http://www.overpass-api.de/api/xapi?map?bbox="+ url[0] + ", " + url[1] + ", " + url[2] + ", " + url[3];


                    $('#overpass').attr("href", overpass);


                });







            });
        </script>
    </body>
</html>