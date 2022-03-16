# Nao-Soccer-Simulator

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
![Stars](https://img.shields.io/github/stars/Robotics-TDP-Team2/Nao-Soccer-Simulator.svg?style=flat&label=Star&maxAge=86400)
[![Github open issues](https://img.shields.io/github/issues-raw/Robotics-TDP-Team2/Nao-Soccer-Simulator.svg)](https://github.com/Robotics-TDP-Team2/Nao-Soccer-Simulator/issues) 
![](https://img.shields.io/github/repo-size/Robotics-TDP-Team2/Nao-Soccer-Simulator.svg?label=Repo%20size&style=flat-square)&nbsp;
![Contributors](https://img.shields.io/github/contributors/Robotics-TDP-Team2/Nao-Soccer-Simulator.svg?style=flat&label=Contributors&maxAge=86400)

#### Contents
* [Synopsis](#synopsis)
* [Phases and Roadmap](#phases-and-roadmap)
* [Usage Examples](#usage-examples)
* [Milestones](#milestones)
* [Contribution Guidelines](#contribution-guidelines)
* [Credits](#credits)
* [Directory Tree](#directory-tree)

## [Synopsis](#Nao-Soccer-Simulator)

As a team design project, we aim to develop a set of robust algorithms to simulate Nao humanoid robot autonomously to play soccer. The project involves designing a pipeline for robot manipulation, path planning, perception, and control. The game is supposed to be played between two teams of Nao robots with each team consisting of 4 players.

## [Phases and Roadmap](#Nao-Soccer-Simulator)

* Phase1: Requirements
![1](https://github.com/Robotics-TDP-Team2/Nao-Soccer-Simulator/blob/main/utils/flowcharts/requirement_stage.png)

* Phase2: Algorithm Development
![2](https://github.com/Robotics-TDP-Team2/Nao-Soccer-Simulator/blob/main/utils/flowcharts/modelling_stage.png)

* Robot Positions
![3](https://github.com/Robotics-TDP-Team2/Nao-Soccer-Simulator/blob/main/utils/flowcharts/roadmap.png)

* Robot Actions
![4](https://github.com/Robotics-TDP-Team2/Nao-Soccer-Simulator/blob/main/utils/flowcharts/robot_actions.png)

## [Usage Examples](#Nao-Soccer-Simulator)

In this section, we illustrate few tutorials to guide users.

## [Milestones](#Nao-Soccer-Simulator)

Latest milestones achieved in the project are listed in this section.

## [Contribution Guidelines](#Nao-Soccer-Simulator)

Thank you for your interest in our project. We strongly encourage reading the contribution guidelines before you be begin which can be found [here](https://github.com/Robotics-TDP-Team2/Nao-Soccer-Simulator/blob/devel/CONTRIBUTION_GUIDELINES.md).

## [Credits](#Nao-Soccer-Simulator)

`Nao-Soccer-Simulator ` is maintained by the RTDP-Project-Team2. Contributors include:

* Adwait Naik
* Ankit Soni
* Bin Liu
* Evelyn Onyi Anyebe
* Shijia Liu
* Xinhe Zheng

## [Directory Tree](#Nao-Soccer-Simulator)

    |–– cmake
    |–– src
    | |–– nao_control
    | | |–– config
    | | |–– launch
    | | |–– msg
    | | |–– scripts
    | | |–– src
    | | |–– srv
    | |–– nao_description
    | | |–– config
    | | |–– launch
    | | |–– models
    | | | |–– materials
    | | | | |–– textures
    | | | |–– meshes
    | | |–– nao_meshes
    | | | |–– meshes
    | | | | |–– V40
    | | | | |–– V41
    | | | |–– rollbackBackupDirectory
    | | | | |–– home
    | | | | | |–– vincent
    | | | |–– texture
    | | |–– scripts
    | | |–– src
    | | |–– urdf
    | | | |–– naoV32_generated_urdf
    | | | |–– naoV33_generated_urdf
    | | | |–– naoV40_generated_urdf
    | | | |–– naoV41_generated_urdf
    | | | |–– naoV42_generated_urdf
    | | | |–– naoV50_generated_urdf
    | |–– nao_gazebo
    | | |–– config
    | | |–– controller
    | | |–– launch
    | | |–– worlds
    | |–– nao_moveit_config
    | | |–– config
    | | |–– launch
    |–– utils
    | |–– codes
    | |–– flowcharts
