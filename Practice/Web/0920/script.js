const button = document.querySelector('#lotto-btn')
button.addEventListener('click', function() {
  // 컨테이너를 만들고
  const ballContainer = document.createElement('div')
  ballContainer.classList.add('ball-container')

  // // 6개의 공을 감싸는 div 만들기
  const ballDiv = document.createElement('div')
  ballDiv.classList.add('ball-div')
  ballContainer.appendChild(ballDiv)

  // 공을 만들어서 =>  6개를 만들어서
  const numbers = _.sampleSize(_.range(1, 46), 6)
  console.log(numbers)
  numbers.sort((a, b) => a - b);
  for (number of numbers) {
    const ball = document.createElement('div')
    ball.classList.add('ball')
    ball.innerText = number
    if (1 <= number & number <= 10) {
      ball.style.background = 'radial-gradient(at 40% 22%, rgb(255, 230, 180), rgb(255 173 24), rgb(217, 138, 0))'
    }
    else if (number <= 20) {
      ball.style.background = 'radial-gradient(at 40% 22%, rgb(201, 225, 255), rgb(71 136 220), rgb(12, 70, 146))'
    }
    else if (number <= 30) {
      ball.style.background = 'radial-gradient(at 40% 22%, rgb(254, 190, 178), rgb(216 82 55), rgb(156, 30, 8))'

    }
    else if (number <= 40) {
      ball.style.background = 'radial-gradient(at 40% 22%, rgb(198, 200, 205), rgb(114 117 124), rgb(52, 53, 53))'

    }
    else if (number <= 45) {
      ball.style.background = 'radial-gradient(at 40% 22%, rgb(156, 219, 151), rgb(32 170 22), rgb(11, 66, 7))'

    }

    // 컨테이너에 붙인다.
    // ballContainer.appendChild(ball)
    ballDiv.appendChild(ball)
  }

  // 컨테이너를 결과 영역에 붙인다. 
  const result = document.querySelector('#result')
  // 번호 뒤에 추가
  // result.appendChild(ballContainer)
  // 번호 앞에 추가
    result.prepend(ballContainer)

})

// 로또 공은 5가지 색깔로 되어 있습니다.
// 1번부터 10번까지는 노란색입니다.
// 11번 부터 20번까지는 파란색입니다.
// 21번부터 30번까지는 빨간색입니다.
// 31번부터 40번까지는 검은색입니다.
// 41번부터 45번까지는 초록색입니다.