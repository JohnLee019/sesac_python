function number_inc(){
            console.log('증가버튼 클릭')
            let number = document.getElementById('result'); 
            let number_string = number.textContent;
            //DIV 요소 안에 있는 글을 가지고 오는 3가지 방식
            //innerText - 글자만 가져온다
            //innerHTML - 글자와 그 태그까지 가져온다 
            //textcontent - 순수 글자만 가져온다
            console.log(number_string);
            let number_string_to_number = Number(number_string);
            let result = number_string_to_number + 1;
            number.textContent = result;
        }
        function number_dec(){
            console.log('감소버튼 클릭')
            let result = document.getElementById('result');
            result.textContent = Number(result.textContent -1);
            //document.getElementById('result').textContent -= 1;로 하면 한줄로도 가능함
        }