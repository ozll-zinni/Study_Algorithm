function solution(numbers, target) {
    var answer = 0;
    
    function dfs(index, current_num){
        if (index == numbers.length) {
            if (current_num == target) {
                answer += 1
            }
            return 
        }
        
        dfs(index+1, current_num + numbers[index])
        dfs(index+1, current_num - numbers[index])   
    }
    dfs(0, 0)
    
    return answer;
}