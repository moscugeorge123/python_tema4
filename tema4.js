const util = require('util');

const fs = require('fs');
precision = 1;

for (let i = 0; i < 10; i++) {
  precision /= 10;
}
// File content
let file_content = fs.readFileSync('m_rar_2018_5.txt', 'utf8');

//
let file_splited = file_content.split('\r\n').filter(e => e != '');
let n = parseInt(file_splited[0]);

file_splited.splice(0, 1);

// B vector
let b = [];

for (let i = 0; i < n; i++) {
  b.push(file_splited[i]);
}

// Matrix
let a = {};
for (let i = n; i < file_splited.length; i++) {
  tmp = file_splited[i].split(/[ ,]+/);
  if (!a[tmp[1]]) {
    a[tmp[1]] = {};
  }

  a[tmp[1]][tmp[2]] = Number.parseFloat(tmp[0]);
}

// Verific daca diagonala are element null
sw = false;
for (let i = 0; i < n; i++) {
  if (typeof a[i][i] === 'undefined') {
    console.log(`[MSG]: ELEMENT NULL PE DIAGOLANA. POZITIA: ${i}`);
    sw = true;
    break;
  }
}

equal = (previos, actual) => {
  for (i = 0; i < previos.length; i++) {
    pr = previos[i];
    nx = actual[i];
    if (
      Math.abs(previos[i] - parseInt(previos[i])) <= precision ||
      Math.abs(parseInt(previos[i]) + 1 - previos[i]) <= precision
    ) {
      pr = parseInt(previos[i]);
    }
    if (
      Math.abs(actual[i] - parseInt(actual[i])) <= precision ||
      Math.abs(parseInt(actual[i]) + 1 - actual[i]) <= precision
    ) {
      nx = parseInt(actual[i]);
    }
    if (pr != nx) return false;
  }
  return true;
};

if (!sw) {
  console.log('[MSG]: ELEMENTE NENULE PE DIAGONALA');

  aCopy = Object.assign({}, a);
  calculatedX = [];
  for (i = 0; i < n; i++) {
    calculatedX.push(Math.floor(Math.random() * 2));
  }
  keys = [];

  for (key of Object.keys(a)) {
    keys[key] = Object.keys(a[key]);
  }

  // previous = calculatedX.map(e => e + 1);
  iterations = 0;
  broken = false;
  do {
    previous = calculatedX.slice();
    iterations++;
    // console.log(previous);

    for (j = 0; j < n; j++) {
      tmpX = 0;
      for (key of keys[j]) {
        if (+key === j) continue;
        // t = a[j][key] * calculatedX[+key];
        // if (!t && t !== 0) {
        //     broken = true;
        //     break;
        // }
        tmpX -= a[j][key] * calculatedX[+key];
      }

      tmpX += +b[j];
      tmpX /= a[j][j];
      calculatedX[j] = tmpX;
    }
  } while (!equal(previous, calculatedX) && iterations < 50000);

  for (i = 0; i < calculatedX.length; i++) {
    fs.appendFile(
      'test.txt',
      `${calculatedX[i]}\n${previous[i]}\n\n`,
      'utf8',
      err => err
    );
  }

  console.log(calculatedX);
  console.log(iterations);

  finalResult = 0;
  for (i = 0; i < n; i++) {
    s = 0;
    for (key of keys[i]) {
      s += a[i][key] * calculatedX[key];
    }

    s -= b[i];
    finalResult += s * s;
  }

  console.log(finalResult);
}
