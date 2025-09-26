#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Task Scheduler for Korean AI Translation Program
Handles scheduling tasks for tomorrow when user is too tired today
"""

import datetime
import json
import os
import re
from typing import Dict, List, Optional

class TaskScheduler:
    def __init__(self, data_file: str = "scheduled_tasks.json"):
        self.data_file = data_file
        self.tasks = self.load_tasks()
    
    def load_tasks(self) -> List[Dict]:
        """Load scheduled tasks from file"""
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except (json.JSONDecodeError, IOError):
                return []
        return []
    
    def save_tasks(self) -> None:
        """Save scheduled tasks to file"""
        try:
            with open(self.data_file, 'w', encoding='utf-8') as f:
                json.dump(self.tasks, f, ensure_ascii=False, indent=2)
        except IOError as e:
            print(f"Failed to save tasks: {e}")
    
    def parse_korean_request(self, text: str) -> Dict:
        """Parse Korean scheduling requests"""
        # Common patterns for scheduling in Korean
        tomorrow_patterns = [
            r'내일.*작업',
            r'내일.*일어나서',
            r'내일.*하자',
            r'내일.*합시다'
        ]
        
        tired_patterns = [
            r'피곤해요',
            r'피곤하다',
            r'지쳤다',
            r'힘들다'
        ]
        
        is_tomorrow_request = any(re.search(pattern, text) for pattern in tomorrow_patterns)
        is_tired = any(re.search(pattern, text) for pattern in tired_patterns)
        
        return {
            'schedule_tomorrow': is_tomorrow_request,
            'reason_tired': is_tired,
            'original_text': text
        }
    
    def schedule_task(self, description: str, schedule_date: Optional[str] = None) -> str:
        """Schedule a task for tomorrow or specified date"""
        if not schedule_date:
            tomorrow = datetime.date.today() + datetime.timedelta(days=1)
            schedule_date = tomorrow.isoformat()
        
        task = {
            'id': len(self.tasks) + 1,
            'description': description,
            'scheduled_date': schedule_date,
            'created_at': datetime.datetime.now().isoformat(),
            'status': 'scheduled'
        }
        
        self.tasks.append(task)
        self.save_tasks()
        
        return f"작업이 {schedule_date}로 예약되었습니다: {description}"
    
    def handle_tired_request(self, request: str) -> str:
        """Handle requests when user is too tired"""
        parsed = self.parse_korean_request(request)
        
        if parsed['schedule_tomorrow'] and parsed['reason_tired']:
            response = self.schedule_task(request)
            return f"이해합니다. 오늘은 휴식하시고 {response}"
        elif parsed['reason_tired']:
            tomorrow = datetime.date.today() + datetime.timedelta(days=1)
            response = self.schedule_task("일반 작업", tomorrow.isoformat())
            return f"피곤하시군요. {response}"
        else:
            return "요청을 이해하지 못했습니다. 다시 설명해 주세요."
    
    def get_tomorrow_tasks(self) -> List[Dict]:
        """Get tasks scheduled for tomorrow"""
        tomorrow = datetime.date.today() + datetime.timedelta(days=1)
        tomorrow_str = tomorrow.isoformat()
        
        return [task for task in self.tasks if task['scheduled_date'] == tomorrow_str]
    
    def get_all_tasks(self) -> List[Dict]:
        """Get all scheduled tasks"""
        return self.tasks
    
    def mark_task_complete(self, task_id: int) -> str:
        """Mark a task as completed"""
        for task in self.tasks:
            if task['id'] == task_id:
                task['status'] = 'completed'
                task['completed_at'] = datetime.datetime.now().isoformat()
                self.save_tasks()
                return f"작업 #{task_id}가 완료로 표시되었습니다."
        
        return f"작업 #{task_id}를 찾을 수 없습니다."

def main():
    """Main function to handle the specific problem statement"""
    scheduler = TaskScheduler()
    
    # Handle the specific request: "내일 일어나서 작업합시다, 오늘은 너무 피곤해요"
    request = "내일 일어나서 작업합시다, 오늘은 너무 피곤해요"
    
    print("Korean AI Task Scheduler")
    print("========================")
    print(f"요청: {request}")
    print()
    
    response = scheduler.handle_tired_request(request)
    print(f"응답: {response}")
    print()
    
    # Show tomorrow's tasks
    tomorrow_tasks = scheduler.get_tomorrow_tasks()
    if tomorrow_tasks:
        print("내일 예정된 작업:")
        for task in tomorrow_tasks:
            print(f"- #{task['id']}: {task['description']} (상태: {task['status']})")
    
    return response

if __name__ == "__main__":
    main()