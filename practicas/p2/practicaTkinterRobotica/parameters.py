#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 4 12:28:18 2023

@author: migue8gl
"""


class Parameters:
    def __init__(self, iterations=50, near=0.5, medium=1.5, far=2.5,
                 min_points=0, max_points=0, distance_threshold=0):
        self._iterations = iterations
        self._near = near
        self._medium = medium
        self._far = far
        self._min_points = min_points
        self._max_points = max_points
        self._distance_threshold = distance_threshold

    # Getters
    def get_iterations(self):
        return self._iterations

    def get_near(self):
        return self._near

    def get_medium(self):
        return self._medium

    def get_far(self):
        return self._far

    def get_min_points(self):
        return self._min_points

    def get_max_points(self):
        return self._max_points

    def get_distance_threshold(self):
        return self._distance_threshold

    # Setters
    def set_iterations(self, value):
        self._iterations = value

    def set_near(self, value):
        self._near = value

    def set_medium(self, value):
        self._medium = value

    def set_far(self, value):
        self._far = value

    def set_min_points(self, value):
        self._min_points = value

    def set_max_points(self, value):
        self._max_points = value

    def set_distance_threshold(self, value):
        self._distance_threshold = value

    def __str__(self):
        return f"Iterations: {self.get_iterations()}, Near: {self.get_near()}, Medium: {self.get_medium()}, Far: {self.get_far()}, Min Points: {self.get_min_points()}, Max Points: {self.get_max_points()}, Distance Threshold: {self.get_distance_threshold()}"
