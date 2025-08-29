import tkinter as tk
from tkinter import ttk, messagebox
import random
import json
import os
from datetime import datetime
import time

class STEMEscapeGame:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("🔓 STEM ESCAPE ROOM CHALLENGE")
        self.root.geometry("1850x1000")
        self.root.configure(bg="#0f0f23")
        self.root.resizable(True, True)
        
        # Game state
        self.game_state = {
            'current_grade': '2',
            'difficulty': 'medium',
            'total_score': 0,
            'current_house': None,
            'current_puzzle': None,
            'hints_remaining': 3,
            'start_time': None,
            'room_start_time': None,
            'completed_houses': [],
            'current_room_puzzles': [],
            'solved_puzzles': [],
            'achievements': [],
            'selected_answer': None
        }
        
        # Difficulty settings
        self.difficulty_settings = {
            'easy': {'puzzles': 3, 'hints': 5, 'time_limit': None},
            'medium': {'puzzles': 4, 'hints': 3, 'time_limit': 900},  # 15 minutes
            'hard': {'puzzles': 6, 'hints': 2, 'time_limit': 600}   # 10 minutes
        }
        
        # Houses data with escape room themes
        self.houses = [
            {
                'id': 'math-mansion',
                'title': '🏰 The Cursed Math Mansion',
                'description': 'Numbers are the key to escape',
                'story': 'You are trapped in an ancient mansion where mathematical curses block every door. Only by solving number puzzles can you break the spells and find your way out!',
                'subject': 'math',
                'bg_color': '#1a0d0d',
                'accent_color': '#8b0000'
            },
            {
                'id': 'science-station',
                'title': '🧪 The Mad Scientist\'s Lab',
                'description': 'Experiments gone wrong - find the cure!',
                'story': 'A mad scientist\'s experiment has locked down the laboratory! You must solve scientific puzzles to reverse the chaos and escape before the lab explodes!',
                'subject': 'science',
                'bg_color': '#0d1a0d',
                'accent_color': '#006400'
            },
            {
                'id': 'tech-tower',
                'title': '💾 The Digital Prison',
                'description': 'Hack your way to freedom',
                'story': 'You\'ve been trapped inside a computer simulation! Use logic and coding skills to hack through the digital barriers and return to the real world!',
                'subject': 'technology',
                'bg_color': '#0d0d1a',
                'accent_color': '#4169e1'
            },
            {
                'id': 'engineering-emporium',
                'title': '⚙️ The Broken Factory',
                'description': 'Fix the machines to unlock the exit',
                'story': 'The factory\'s safety systems have malfunctioned, trapping you inside! Solve engineering puzzles to repair the machines and activate the emergency exit!',
                'subject': 'engineering',
                'bg_color': '#1a1a0d',
                'accent_color': '#ff8c00'
            }
        ]
        
        # Current screen tracking
        self.current_screen = None
        self.timer_running = False
        self.time_remaining = 0
        
        # Load saved game state
        self.load_game_state()
        
        # Initialize UI
        self.show_homepage()
    
    def clear_screen(self):
        """Clear all widgets from the screen"""
        for widget in self.root.winfo_children():
            widget.destroy()
        self.timer_running = False
    
            tk.Label(diff_frame, text="🎚️ Danger Level:", font=('Arial', 14, 'bold'), 
                fg='#ecf0f1', bg='#34495e').pack(pady=10)
        
        self.difficulty_var = tk.StringVar(value=self.game_state['difficulty'])
        
        diff_button_frame = tk.Frame(diff_frame, bg='#34495e')
        diff_button_frame.pack(pady=5)
        
        diff_colors = {'easy': '#27ae60', 'medium': '#f39c12', 'hard': '#e74c3c'}
        diff_labels = {'easy': '🟢 EASY', 'medium': '🟡 MEDIUM', 'hard': '🔴 HARD'}
        
        for diff in ['easy', 'medium', 'hard']:
            btn = tk.Radiobutton(diff_button_frame, text=diff_labels[diff], 
                               variable=self.difficulty_var, value=diff, 
                               font=('Arial', 12, 'bold'), fg='white', 
                               bg=diff_colors[diff], selectcolor=diff_colors[diff],
                               command=self.on_difficulty_change, relief='raised', bd=2)
            btn.pack(side='left', padx=15, pady=5)
        
        # Start mission button
        start_btn = tk.Button(setup_frame, text="🚨 BEGIN ESCAPE MISSION 🚨", 
                            font=('Arial', 18, 'bold'), fg='white', bg='#e74c3c', 
                            relief='raised', bd=3, pady=15,
                            command=self.start_game)
        start_btn.pack(pady=30)
        
        # Buttons frame
        button_frame = tk.Frame(setup_frame, bg='#2c3e50')
        button_frame.pack(pady=10)
        
        help_btn = tk.Button(button_frame, text="❓ Mission Instructions", 
                           font=('Arial', 12, 'bold'), fg='white', bg='#3498db', 
                           relief='raised', bd=2, command=self.show_help)
        help_btn.pack(side='left', padx=10)
        
        reset_btn = tk.Button(button_frame, text="🔄 Reset Progress", 
                            font=('Arial', 12, 'bold'), fg='white', bg='#95a5a6', 
                            relief='raised', bd=2, command=self.reset_game)
        reset_btn.pack(side='right', padx=10)
    
    def show_neighborhood(self):
        """Display the neighborhood map screen with escape room theme"""
        self.current_screen = 'neighborhood'
        self.clear_screen()
        
        # Main frame
        main_frame = tk.Frame(self.root, bg="#0f0f23", relief='raised', bd=3)
        main_frame.pack(expand=True, fill='both', padx=5, pady=5)
        
        # Header frame
        header_frame = tk.Frame(main_frame, bg='#1a1a2e', relief='sunken', bd=2, height=100)
        header_frame.pack(fill='x', padx=5, pady=5)
        header_frame.pack_propagate(False)
        
g        # Back button
        back_btn = tk.Button(header_frame, text="🏠 Return to Base", font=('Arial', 11, 'bold'),
                           fg='white', bg='#7f8c8d', relief='raised', bd=2,
                           command=self.show_homepage)
        back_btn.place(x=10, y=10)
        
        # Title
        title_label = tk.Label(header_frame, text="🌃 CHOOSE YOUR ESCAPE CHALLENGE", 
                              font=('Arial', 22, 'bold'), fg='#e74c3c', bg='#1a1a2e')
        title_label.pack(pady=15)
        
        # Mission status HUD
        hud_frame = tk.Frame(header_frame, bg='#2c3e50', relief='groove', bd=2)
        hud_frame.pack(fill='x', padx=20, pady=5)
        
        # Progress and score
        progress_text = f"🏆 MISSIONS COMPLETED: {len(self.game_state['completed_houses'])}/{len(self.houses)}"
        tk.Label(hud_frame, text=progress_text, font=('Arial', 12, 'bold'), 
                fg='#f39c12', bg='#2c3e50').pack(side='left', padx=10, pady=5)
        
        score_text = f"💯 TOTAL SCORE: {self.game_state['total_score']}"
        tk.Label(hud_frame, text=score_text, font=('Arial', 12, 'bold'), 
                fg='#27ae60', bg='#2c3e50').pack(side='right', padx=10, pady=5)
        
        # Achievements ticker
        if self.game_state['achievements']:
            achievements_text = "🏅 " + " | ".join(self.game_state['achievements'][-3:])
            tk.Label(hud_frame, text=achievements_text, font=('Arial', 10, 'bold'), 
                    fg='white', bg='#8e44ad', relief='raised', bd=1).pack(pady=3)
        
        # Houses frame
        houses_frame = tk.Frame(main_frame, bg='#16213e')
        houses_frame.pack(expand=True, fill='both', padx=10, pady=10)
        
        # Create escape room grid
        for i, house in enumerate(self.houses):
            row = i // 2
            col = i % 2
            
            # Check status
            is_locked = i > 0 and self.houses[i-1]['id'] not in self.game_state['completed_houses']
            is_completed = house['id'] in self.game_state['completed_houses']
            
            # House frame with themed colors
            house_frame = tk.Frame(houses_frame, bg=house['bg_color'], relief='raised', bd=3, 
                                 width=500, height=250)
            house_frame.grid(row=row, column=col, padx=15, pady=15, sticky='nsew')
            house_frame.pack_propagate(False)
            
            # Configure grid
            houses_frame.grid_rowconfigure(row, weight=1)
            houses_frame.grid_columnconfigure(col, weight=1)
            
            # House title
            tk.Label(house_frame, text=house['title'], font=('Arial', 16, 'bold'), 
                    fg=house['accent_color'], bg=house['bg_color']).pack(pady=10)
            
            # House description
            tk.Label(house_frame, text=house['description'], font=('Arial', 12, 'italic'), 
                    fg='#ecf0f1', bg=house['bg_color']).pack(pady=5)
            
            # Difficulty info
            difficulty_info = self.difficulty_settings[self.game_state['difficulty']]
            puzzle_count = difficulty_info['puzzles']
            hint_count = difficulty_info['hints']
            time_limit = difficulty_info['time_limit']
            
            if time_limit:
                info_text = f"⏱️ {puzzle_count} Puzzles • {hint_count} Hints • {time_limit//60}min Limit"
            else:
                info_text = f"🧩 {puzzle_count} Puzzles • {hint_count} Hints Available"
            
            tk.Label(house_frame, text=info_text, font=('Arial', 10), 
                    fg='#bdc3c7', bg=house['bg_color']).pack(pady=5)
            
            # Status and action
            if is_completed:
                tk.Label(house_frame, text="✅ MISSION COMPLETE", font=('Arial', 12, 'bold'), 
                        fg='#27ae60', bg=house['bg_color']).pack(pady=10)
                
                replay_btn = tk.Button(house_frame, text="🔄 Replay Mission", 
                                     font=('Arial', 11, 'bold'), fg='white', bg='#3498db',
                                     relief='raised', bd=2, 
                                     command=lambda h=house['id']: self.enter_house(h))
                replay_btn.pack(pady=5)
                
            elif is_locked:
                tk.Label(house_frame, text="🔒 LOCKED", font=('Arial', 12, 'bold'), 
                        fg='#e74c3c', bg=house['bg_color']).pack(pady=10)
                tk.Label(house_frame, text="Complete previous mission first!", 
                        font=('Arial', 10), fg='#95a5a6', bg=house['bg_color']).pack()
                
            else:
                danger_btn = tk.Button(house_frame, text="⚠️ ENTER DANGER ZONE ⚠️", 
                                     font=('Arial', 13, 'bold'), fg='white', 
                                     bg=house['accent_color'], relief='raised', bd=3,
                                     command=lambda h=house['id']: self.enter_house(h))
                danger_btn.pack(pady=15)
        
        # Leaderboard button
        leaderboard_btn = tk.Button(main_frame, text="🏆 VIEW HALL OF FAME", 
                                   font=('Arial', 12, 'bold'), fg='white', bg='#8e44ad',
                                   relief='raised', bd=2, command=self.show_leaderboard)
        leaderboard_btn.pack(pady=10)
    
    
    
    def enter_house(self, house_id):
    """Enter a specific escape room"""
    house = next(h for h in self.houses if h['id'] == house_id)
    
    self.game_state['current_house'] = house_id
    self.game_state['hints_remaining'] = self.difficulty_settings[self.game_state['difficulty']]['hints']
    self.game_state['room_start_time'] = time.time()
    
    # Set up timer if difficulty requires it
    time_limit = self.difficulty_settings[self.game_state['difficulty']]['time_limit']
    if time_limit:
        self.time_remaining = time_limit
        self.timer_running = True
    
    self.generate_room_puzzles(house)
    self.show_escape_room(house)


def generate_room_puzzles(self, house):
    """Generate puzzles for the current escape room"""
    num_puzzles = self.difficulty_settings[self.game_state['difficulty']]['puzzles']
    self.game_state['current_room_puzzles'] = []
    self.game_state['solved_puzzles'] = []
    
    puzzle_types = self.get_puzzle_types_for_subject(house['subject'])
    
    for i in range(num_puzzles):
        puzzle_type = puzzle_types[i % len(puzzle_types)]
        puzzle = self.generate_puzzle(puzzle_type)
        self.game_state['current_room_puzzles'].append({
            'id': f"puzzle-{i}",
            'type': puzzle_type,
            **puzzle,
            'solved': False
        })
    
    # Reset selected answer
    self.game_state['selected_answer'] = None


def show_escape_room(self, house):
    """Display the main escape room interface"""
    self.current_screen = 'escape_room'
    self.clear_screen()
    
    # Main container
    main_frame = tk.Frame(self.root, bg=house['bg_color'], relief='sunken', bd=3)
    main_frame.pack(expand=True, fill='both', padx=3, pady=3)
    
    # Header with mission info
    header_frame = tk.Frame(main_frame, bg='#1a1a1a', relief='raised', bd=2, height=120)
    header_frame.pack(fill='x', padx=5, pady=5)
    header_frame.pack_propagate(False)
    
    # Back button
    back_btn = tk.Button(header_frame, text="🚪 ABORT MISSION", font=('Arial', 10, 'bold'),
                         fg='white', bg='#e74c3c', relief='raised', bd=2,
                         command=self.show_neighborhood)
    back_btn.place(x=10, y=10)
    
    # Room title and story
    title_label = tk.Label(header_frame, text=house['title'],
                           font=('Arial', 18, 'bold'),
                           fg=house['accent_color'], bg='#1a1a1a')
    title_label.pack(pady=5)
    
    story_label = tk.Label(header_frame, text=house['story'],
                           font=('Arial', 11, 'italic'),
                           fg='#ecf0f1', bg='#1a1a1a')
    story_label.pack(pady=5)

