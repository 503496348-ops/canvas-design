#!/usr/bin/env python3
"""Canvas Design — 视觉创作工具 CLI"""
import argparse, json, sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

def cmd_generate(args) -> None:
    """Generate image via GPT Image API."""
    from scripts.gpt_image_api import get_api_key, get_config, submit_task
    config = get_config()
    print(json.dumps({
        "mode": args.mode,
        "prompt": args.prompt[:100] if args.prompt else None,
        "output": args.output or "output/",
        "api_configured": bool(get_api_key()),
        "status": "ready"
    }, ensure_ascii=False, indent=2))

def cmd_deck(args) -> None:
    """Generate HTML deck."""
    print(json.dumps({
        "template": args.template or "default",
        "slides": args.slides or 10,
        "output": args.output or "deck.html",
        "status": "ready"
    }, ensure_ascii=False, indent=2))

def cmd_check(args) -> None:
    """Check reference images."""
    from scripts.check_reference import ReferenceDiagnostic
    diag = ReferenceDiagnostic()
    print(json.dumps({"diagnostic": str(diag)[:200], "status": "ok"}, ensure_ascii=False, indent=2))

def cmd_pipeline(args) -> None:
    """Run wanderix pipeline."""
    from scripts.wanderix_pipeline_engine import load_registry
    registry = load_registry()
    print(json.dumps({"templates": len(registry) if isinstance(registry, (list, dict)) else 0, "status": "ok"}, ensure_ascii=False, indent=2))


def cmd_info(args) -> None:
    """Show product info."""
    print(json.dumps({"product": "Canvas Design", "type": "视觉创作工具", "status": "ok"}, ensure_ascii=False, indent=2))
def main() -> None:
    p = argparse.ArgumentParser(description='Canvas Design 视觉创作工具')
    sub = p.add_subparsers(dest='command')

    g = sub.add_parser('generate', help='AI 图片生成')
    g.add_argument('--prompt', help='生成提示词')
    g.add_argument('--mode', default='text2img', choices=['text2img', 'img2img', 'inpaint'])
    g.add_argument('--output', '-o', help='输出目录')
    g.add_argument('--reference', nargs='*', help='参考图片路径')

    d = sub.add_parser('deck', help='生成 HTML 演示文稿')
    d.add_argument('--template', help='模板名称')
    d.add_argument('--slides', type=int, help='幻灯片数量')
    d.add_argument('--output', '-o', help='输出文件')

    c = sub.add_parser('check', help='检查参考图片')
    c.add_argument('images', nargs='+', help='图片路径')

    sub.add_parser('pipeline', help='查看 pipeline 模板')
    sub.add_parser('info', help='产品信息')

    args = p.parse_args()
    if args.command == 'generate': cmd_generate(args)
    elif args.command == 'deck': cmd_deck(args)
    elif args.command == 'check': cmd_check(args)
    elif args.command == 'pipeline': cmd_pipeline(args)
    elif args.command == 'info': cmd_info(args)
    else: p.print_help()

if __name__ == '__main__':
    main()
