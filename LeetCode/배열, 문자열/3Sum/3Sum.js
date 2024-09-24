var threeSum = function(nums) {
    // 1단계: 배열 정렬
    nums.sort((a, b) => a - b);
    
    let result = [];
    
    // 2단계: 배열 순회
    for (let i = 0; i < nums.length - 2; i++) {
        // 4단계: 현재 요소가 이전 요소와 같다면 중복이므로 건너뛰기
        if (i > 0 && nums[i] === nums[i - 1]) continue;
        
        // 3단계: 두 포인터 방식
        let left = i + 1;
        let right = nums.length - 1;
        
        while (left < right) {
            let sum = nums[i] + nums[left] + nums[right];
            
            if (sum === 0) {
                // 트리플렛을 찾았을 때
                result.push([nums[i], nums[left], nums[right]]);
                
                // 4단계: 중복된 값 건너뛰기
                while (left < right && nums[left] === nums[left + 1]) left++;
                while (left < right && nums[right] === nums[right - 1]) right--;
                
                // 포인터 이동
                left++;
                right--;
            } else if (sum < 0) {
                // 합이 0보다 작으면 왼쪽 포인터를 이동해서 합을 키운다
                left++;
            } else {
                // 합이 0보다 크면 오른쪽 포인터를 이동해서 합을 줄인다
                right--;
            }
        }
    }
    
    return result;
};
