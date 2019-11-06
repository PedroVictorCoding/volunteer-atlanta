
            var array_save = [];
        function setup() {
            stroke(255);
            var newcnv = createCanvas(200, 100);
            background(51);
            for (var i = 0; i < array_save.length; i++) {
              strokeWeight(4);
              line(array_save[i].split(",")[0], array_save[i].split(",")[1],array_save[i].split(",")[2], array_save[i].split(",")[3])
              console.log(array_save);
            };
            newcnv.parent('StoredSignature');
        }
