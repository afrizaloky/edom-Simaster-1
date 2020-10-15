// 1 = Sangat Baik
// 2 = Baik
// 3 = Cukup
// 4 = Kurang
var nilai = "2"; // Edit penilaian dosen

for (i = 0; i < 13; i++) {
  var elements = document.getElementsByName(
    "jawabanInstrumenPilihan[" + i + "]"
  );
  for (j = 0; j < elements.length; j++) {
    if (elements[j].value == nilai) {
      elements[j].checked = true;
    }
  }
}

// Run it in console