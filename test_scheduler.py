#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Simple test for the task scheduler functionality
"""

import os
import tempfile
from task_scheduler import TaskScheduler

def test_korean_parsing():
    """Test Korean text parsing functionality"""
    scheduler = TaskScheduler()
    
    # Test case 1: The original problem statement
    text1 = "내일 일어나서 작업합시다, 오늘은 너무 피곤해요"
    result1 = scheduler.parse_korean_request(text1)
    
    assert result1['schedule_tomorrow'] == True, "Should recognize tomorrow scheduling request"
    assert result1['reason_tired'] == True, "Should recognize tired reason"
    
    # Test case 2: Only tired, no tomorrow mention
    text2 = "오늘은 피곤해요"
    result2 = scheduler.parse_korean_request(text2)
    
    assert result2['schedule_tomorrow'] == False, "Should not recognize tomorrow scheduling"
    assert result2['reason_tired'] == True, "Should recognize tired reason"
    
    print("✅ Korean parsing tests passed")

def test_task_scheduling():
    """Test task scheduling functionality"""
    # Use temporary file for testing
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.json') as tmp:
        tmp_file = tmp.name
    
    try:
        scheduler = TaskScheduler(tmp_file)
        
        # Test scheduling a task
        response = scheduler.schedule_task("테스트 작업")
        assert "예약되었습니다" in response, "Should confirm task scheduling"
        
        # Test handling tired request
        request = "내일 일어나서 작업합시다, 오늘은 너무 피곤해요"
        response = scheduler.handle_tired_request(request)
        assert "이해합니다" in response, "Should show understanding"
        assert "휴식하시고" in response, "Should suggest rest"
        
        print("✅ Task scheduling tests passed")
        
    finally:
        # Clean up
        if os.path.exists(tmp_file):
            os.unlink(tmp_file)

def main():
    """Run all tests"""
    print("Task Scheduler Test Suite")
    print("========================")
    
    try:
        test_korean_parsing()
        test_task_scheduling()
        print("\n🎉 All tests passed!")
        
    except AssertionError as e:
        print(f"\n❌ Test failed: {e}")
        return 1
    except Exception as e:
        print(f"\n💥 Unexpected error: {e}")
        return 1
    
    return 0

if __name__ == "__main__":
    exit(main())