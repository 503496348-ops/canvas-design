# 艺游未境 × ControlNet 融合增强

## 融合来源
- **竞品**: lllyasviel/ControlNet (30K⭐)
- **核心能力**: 10种空间控制条件 + 零卷积训练安全 + 多控制融合

## 新增模块

### control_processors.py
空间控制信号处理器，支持6种控制类型：
- `CannyProcessor`: Canny边缘检测（带阈值参数）
- `DepthProcessor`: 深度图估计（MiDaS + 梯度回退）
- `PoseProcessor`: 人体姿态估计（骨架提取）
- `ScribbleProcessor`: 涂鸦/线稿提取
- `SegmentationProcessor`: 语义分割图（ADE20K色表）
- `MLSDProcessor`: 直线检测（Hough变换）
- 统一API: `process_control(image, ControlType.CANNY)`

### control_fusion.py
多控制信号融合引擎：
- `ControlFuser`: 加权融合 + 多混合模式（ADD/MAX/OVERLAY/MULTIPLY）
- `StrengthScheduler`: 步进强度调度（常量/线性/余弦/阶梯/自定义）
- 预设配置: balanced / cascaded / composition

### conditioning_pipeline.py
端到端条件化流水线：
- 输入预处理 → 控制提取 → 控制融合 → 零卷积 → 张量生成
- 模型预设: SD1.5 / SDXL / Flux
- 便捷API: `quick_condition()` / `multi_control_condition()`
- ControlNet零卷积初始化（权重和偏置均为零）

## 用法

```python
from control_processors import process_control, ControlType, process_multi_control
from control_fusion import ControlFuser, StrengthScheduler, create_balanced_fusion
from conditioning_pipeline import ConditioningPipeline, ConditioningConfig, quick_condition

# 1. 单控制
result = quick_condition("photo.jpg", control_type="canny", strength=0.8)

# 2. 多控制融合
result = multi_control_condition(
    "photo.jpg",
    controls=["canny", "depth"],
    weights=[0.6, 0.4],
)

# 3. 自定义流水线
config = ConditioningConfig(
    control_types=["canny", "depth", "pose"],
    control_weights=[0.5, 0.3, 0.2],
    global_strength=0.85,
    resolution=(1024, 1024),
)
pipeline = ConditioningPipeline(config)
result = pipeline.run("photo.jpg", prompt="a beautiful landscape")
```
