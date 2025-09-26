#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Main entry point for Korean AI Translation Program with Task Scheduling
"""

from task_scheduler import TaskScheduler

def main():
    """Main program entry point"""
    print("한국어 AI 번역 프로그램 - 작업 스케줄러")
    print("=====================================")
    
    scheduler = TaskScheduler()
    
    # Handle the specific problem statement
    problem_statement = "내일 일어나서 작업합시다, 오늘은 너무 피곤해요."
    
    print(f"입력: {problem_statement}")
    print()
    
    # Process the request
    response = scheduler.handle_tired_request(problem_statement)
    print(f"시스템 응답: {response}")
    print()
    
    # Show scheduled tasks
    tasks = scheduler.get_tomorrow_tasks()
    if tasks:
        print("예약된 작업:")
        for task in tasks:
            print(f"  📅 {task['scheduled_date']}: {task['description']}")
            print(f"     상태: {task['status']}")
            print(f"     생성일: {task['created_at']}")
            print()

if __name__ == "__main__":
    main()