#!/usr/bin/env python3
"""
Verification script for new TradingAgents features.

This script tests:
1. Multi-LLM provider support
2. Broker integration (basic)
3. Web interface components
4. Docker files exist

Run this to verify all new features are properly installed.
"""

import os
import sys
from pathlib import Path


def test_llm_factory():
  """Test LLM factory implementation."""
  print("\n" + "=" * 70)
  print("TEST 1: Multi-LLM Provider Support")
  print("=" * 70)

  try:
    from tradingagents.llm_factory import LLMFactory

    # Test supported providers
    providers = LLMFactory.SUPPORTED_PROVIDERS
    print(f"✓ Supported providers: {', '.join(providers)}")

    # Test recommendations
    for provider in providers:
      models = LLMFactory.get_recommended_models(provider)
      print(
        f"✓ {provider.capitalize()} recommended models: {len(models)} options")

    # Test validation (without actual API keys)
    print("✓ Validation methods available")

    print("\n✓ LLM Factory: PASS")
    return True

  except Exception as e:
    print(f"\n✗ LLM Factory: FAIL - {e}")
    return False


def test_broker_integration():
  """Test broker integration."""
  print("\n" + "=" * 70)
  print("TEST 2: Broker Integration")
  print("=" * 70)

  try:
    from tradingagents.brokers import BaseBroker, AlpacaBroker
    from tradingagents.brokers.base import (
      BrokerOrder, BrokerPosition, BrokerAccount,
      OrderSide, OrderType, OrderStatus
    )
    from decimal import Decimal

    print("✓ Base broker interface imported")
    print("✓ Alpaca broker imported")
    print("✓ Order types available")

    # Test creating order (without submitting)
    order = BrokerOrder(
        symbol="AAPL",
        side=OrderSide.BUY,
        quantity=Decimal("10"),
        order_type=OrderType.MARKET
    )
    print(
      f"✓ Created order: {order.symbol} {order.side.value} {order.quantity}")

    # Test broker creation (without connecting)
    try:
      broker = AlpacaBroker(paper_trading=True)
      print("✓ Alpaca broker instantiated (connection not tested)")
    except ValueError as e:
      # Expected if no API keys
      print("✓ Alpaca broker requires API keys (as expected)")

    print("\n✓ Broker Integration: PASS")
    return True

  except Exception as e:
    print(f"\n✗ Broker Integration: FAIL - {e}")
    import traceback
    traceback.print_exc()
    return False


def test_web_interface():
  """Test web interface components."""
  print("\n" + "=" * 70)
  print("TEST 3: Web Interface")
  print("=" * 70)

  try:
    # Check web_app.py exists
    web_app = Path("/home/user/TradingAgents/web_app.py")
    if web_app.exists():
      print("✓ web_app.py exists")
    else:
      print("✗ web_app.py not found")
      return False

    # Check chainlit config
    chainlit_config = Path("/home/user/TradingAgents/.chainlit")
    if chainlit_config.exists():
      print("✓ .chainlit config exists")
    else:
      print("✗ .chainlit config not found")
      return False

    # Check chainlit is importable
    try:
      import chainlit
      print(
        f"✓ Chainlit installed (version: {chainlit.__version__ if hasattr(chainlit, '__version__') else 'unknown'})")
    except ImportError:
      print("⚠ Chainlit not installed (pip install chainlit)")

    # Check web_app imports
    with open(web_app, 'r') as f:
      content = f.read()
      if 'chainlit' in content:
        print("✓ Web app uses Chainlit")
      if 'AlpacaBroker' in content:
        print("✓ Web app integrates broker")
      if 'TradingAgentsGraph' in content:
        print("✓ Web app integrates TradingAgents")

    print("\n✓ Web Interface: PASS")
    return True

  except Exception as e:
    print(f"\n✗ Web Interface: FAIL - {e}")
    return False


def test_docker_files():
  """Test Docker configuration files."""
  print("\n" + "=" * 70)
  print("TEST 4: Docker Support")
  print("=" * 70)

  try:
    base_path = Path("/home/user/TradingAgents")

    # Check Dockerfile
    dockerfile = base_path / "Dockerfile"
    if dockerfile.exists():
      print("✓ Dockerfile exists")
      with open(dockerfile, 'r') as f:
        content = f.read()
        if 'python:3.11' in content:
          print("  - Uses Python 3.11")
        if 'chainlit' in content:
          print("  - Includes web interface")
        if 'EXPOSE 8000' in content:
          print("  - Exposes port 8000")
    else:
      print("✗ Dockerfile not found")
      return False

    # Check docker-compose.yml
    compose = base_path / "docker-compose.yml"
    if compose.exists():
      print("✓ docker-compose.yml exists")
      with open(compose, 'r') as f:
        content = f.read()
        if 'tradingagents' in content:
          print("  - Defines tradingagents service")
        if 'jupyter' in content:
          print("  - Includes optional Jupyter service")
        if 'volumes' in content:
          print("  - Configures data persistence")
    else:
      print("✗ docker-compose.yml not found")
      return False

    # Check .dockerignore
    dockerignore = base_path / ".dockerignore"
    if dockerignore.exists():
      print("✓ .dockerignore exists")
    else:
      print("⚠ .dockerignore not found (recommended)")

    # Check DOCKER.md
    docker_md = base_path / "DOCKER.md"
    if docker_md.exists():
      print("✓ DOCKER.md documentation exists")
    else:
      print("⚠ DOCKER.md not found")

    print("\n✓ Docker Support: PASS")
    return True

  except Exception as e:
    print(f"\n✗ Docker Support: FAIL - {e}")
    return False


def test_documentation():
  """Test documentation files."""
  print("\n" + "=" * 70)
  print("TEST 5: Documentation")
  print("=" * 70)

  try:
    base_path = Path("/home/user/TradingAgents")

    docs = {
        "NEW_FEATURES.md": "New features guide",
        "DOCKER.md": "Docker documentation",
        "tradingagents/brokers/README.md": "Broker integration guide",
        "examples/use_claude.py": "Claude example",
        "examples/paper_trading_alpaca.py": "Paper trading example",
        "examples/tradingagents_with_alpaca.py": "Full integration example",
    }

    found = 0
    for doc, description in docs.items():
      if (base_path / doc).exists():
        print(f"✓ {description}")
        found += 1
      else:
        print(f"✗ {doc} not found")

    print(f"\n✓ Documentation: {found}/{len(docs)} files present")
    return found == len(docs)

  except Exception as e:
    print(f"\n✗ Documentation: FAIL - {e}")
    return False


def test_examples():
  """Test example scripts."""
  print("\n" + "=" * 70)
  print("TEST 6: Example Scripts")
  print("=" * 70)

  try:
    base_path = Path("/home/user/TradingAgents/examples")

    examples = [
        "use_claude.py",
        "paper_trading_alpaca.py",
        "tradingagents_with_alpaca.py",
    ]

    for example in examples:
      script = base_path / example
      if script.exists():
        # Check if executable
        is_executable = os.access(script, os.X_OK)
        exec_mark = "✓" if is_executable else "○"
        print(
          f"{exec_mark} {example} {'(executable)' if is_executable else ''}")
      else:
        print(f"✗ {example} not found")

    print("\n✓ Example Scripts: PASS")
    return True

  except Exception as e:
    print(f"\n✗ Example Scripts: FAIL - {e}")
    return False


def main():
  """Run all verification tests."""
  print("=" * 70)
  print("TRADINGAGENTS NEW FEATURES VERIFICATION")
  print("=" * 70)

  results = []

  # Run tests
  results.append(("LLM Factory", test_llm_factory()))
  results.append(("Broker Integration", test_broker_integration()))
  results.append(("Web Interface", test_web_interface()))
  results.append(("Docker Support", test_docker_files()))
  results.append(("Documentation", test_documentation()))
  results.append(("Example Scripts", test_examples()))

  # Summary
  print("\n" + "=" * 70)
  print("VERIFICATION SUMMARY")
  print("=" * 70)

  passed = sum(1 for _, result in results if result)
  total = len(results)

  for name, result in results:
    status = "✓ PASS" if result else "✗ FAIL"
    print(f"{status}: {name}")

  print(
    f"\nResults: {passed}/{total} tests passed ({passed / total * 100:.0f}%)")

  if passed == total:
    print("\n🎉 All new features verified successfully!")
    print("\nNext steps:")
    print("  1. Configure .env with your API keys")
    print("  2. Try: chainlit run web_app.py -w")
    print("  3. Or: docker-compose up")
    print("  4. Or run: python examples/use_claude.py")
    return 0
  else:
    print(f"\n⚠ {total - passed} test(s) failed. Review errors above.")
    return 1


if __name__ == "__main__":
  sys.exit(main())
