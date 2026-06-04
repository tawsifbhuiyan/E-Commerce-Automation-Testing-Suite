"""
Main entry point for the E-commerce Automation Testing Suite
"""
import sys
import traceback

def main():
    """Main function to run the automation suite"""
    print("""
    ╔═══════════════════════════════════════════════════════════════╗
    ║                                                               ║
    ║   🤖 E-COMMERCE AUTOMATION TESTING SUITE v2.0               ║
    ║                                                               ║
    ║   Features:                                                   ║
    ║   • Multi-site automated testing                            ║
    ║   • Modular class-based architecture                        ║
    ║   • Automatic screenshot capture                            ║
    ║   • Professional HTML reports                               ║
    ║                                                               ║
    ╚═══════════════════════════════════════════════════════════════╝
    """)
    
    try:
        from scripts.test_runner import TestRunner
        runner = TestRunner()
        
        try:
            runner.setup()
            report_path = runner.run_all_tests()
            print(f"\n✨ Test suite completed successfully!")
            print(f"📄 Open the report to view details: {report_path}")
            
        except KeyboardInterrupt:
            print("\n⚠️ Test execution interrupted by user")
            sys.exit(1)
        except Exception as e:
            print(f"\n❌ Fatal error during test execution: {str(e)}")
            traceback.print_exc()
            sys.exit(1)
        finally:
            runner.teardown()
            
    except ImportError as e:
        print(f"\n❌ Import error: {str(e)}")
        print("\nMake sure all required files exist:")
        print("  - config.py")
        print("  - webdriver_factory.py")
        print("  - screenshot_manager.py")
        print("  - report_generator.py")
        print("  - test_base.py")
        print("  - test_amazon.py")
        print("  - test_flipkart.py")
        print("  - test_bestbuy.py")
        print("  - test_target.py")
        print("  - test_walmart.py")
        print("  - test_ebay.py")
        print("  - test_myntra.py")
        print("  - test_runner.py")
        sys.exit(1)

if __name__ == "__main__":
    main()