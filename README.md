# Sim2Real
Implement Nvidia AI Lab's paper "Towards Optimal Strategies for Training Self-Driving Perception Models in Simulation" based on "Lift, Splat, Shoot"

## Project Structure
- carla_data_generation
Generate nuScence style like Carla dataset including six cameras around the ego vehicle, Lidar, Town03 maps, and annotations of pedestrain and vehicles.

- style_transform
Use MUNIT style transform baseline to train synthesis to cityscape style transform model with Carla dataset and NuScene mini dataset.

- lift_splat_shoot
Based on the "Lift Splat Shoot" BEV segmentation model, train lift_splat model with original Carla dataset and lift_splat_adpat model with style transformed Carla dataset from scratch.

Comparing the performance of lift_splat_adpat model and lift_splat model on target domain (NuScene) to certificate the base theory, "domain adaption", is a way to implement Sim2Real.

## Project Result
- lift-splat model: https://drive.google.com/file/d/1wffumYyAfn_brq2O2dLMcCCZHNqBLNAY/view?usp=sharing
- oracle model: https://drive.google.com/file/d/1LopHcfHabsJ0Fah_SLTdgxFAf7JE5leY/view?usp=sharing

## Project Analysis

## Reference Announcement
1. The paper "Towards Optimal Strategies for Training Self-Driving Perception Models in Simulation"
2. The paper and source code "Lift, Splat, Shoot: Encoding Images From Arbitrary Camera Rigs by Implicitly Unprojecting to 3D", https://github.com/nv-tlabs/lift-splat-shoot
3. Carla Dataset Generator: https://github.com/cf206cd/carla_nuscenes
4. MUNIT source code: https://github.com/NVlabs/MUNIT
