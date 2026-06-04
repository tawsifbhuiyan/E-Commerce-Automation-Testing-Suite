"""
Generates comprehensive HTML test reports
"""
import os
from datetime import datetime
from typing import List, Dict

class ReportGenerator:
    """Generates HTML reports for test execution"""
    
    def __init__(self, report_dir: str):
        self.report_dir = report_dir
        self.test_results: List[Dict] = []
        
    def add_result(self, test_name: str, status: str, message: str, screenshot: str = ""):
        """Add a test result to the report"""
        self.test_results.append({
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "test_name": test_name,
            "status": status,
            "message": message,
            "screenshot": screenshot
        })
    
    def generate_report(self) -> str:
        """Generate HTML report and return file path"""
        total = len(self.test_results)
        passed = sum(1 for r in self.test_results if r['status'] == 'PASS')
        failed = sum(1 for r in self.test_results if r['status'] == 'FAIL')
        warnings = sum(1 for r in self.test_results if r['status'] == 'WARNING')
        
        html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>E-Commerce Automation Test Report</title>
            <style>
                * {{ margin: 0; padding: 0; box-sizing: border-box; }}
                body {{ font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 20px; }}
                .container {{ max-width: 1400px; margin: 0 auto; background: white; border-radius: 15px; box-shadow: 0 20px 60px rgba(0,0,0,0.3); overflow: hidden; }}
                .header {{ background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; padding: 30px; text-align: center; }}
                .header h1 {{ font-size: 2.5em; margin-bottom: 10px; }}
                .stats {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 20px; padding: 30px; background: #f8f9fa; }}
                .stat-card {{ background: white; padding: 20px; border-radius: 10px; text-align: center; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }}
                .stat-card .number {{ font-size: 2.5em; font-weight: bold; }}
                .stat-card .label {{ color: #666; margin-top: 10px; }}
                .pass-count .number {{ color: #28a745; }}
                .fail-count .number {{ color: #dc3545; }}
                .warn-count .number {{ color: #ffc107; }}
                .results {{ padding: 30px; }}
                table {{ width: 100%; border-collapse: collapse; }}
                th, td {{ padding: 15px; text-align: left; border-bottom: 1px solid #ddd; }}
                th {{ background: #667eea; color: white; position: sticky; top: 0; }}
                tr:hover {{ background: #f5f5f5; }}
                .status-badge {{ padding: 5px 10px; border-radius: 5px; font-weight: bold; display: inline-block; }}
                .status-PASS {{ background: #d4edda; color: #155724; }}
                .status-FAIL {{ background: #f8d7da; color: #721c24; }}
                .status-WARNING {{ background: #fff3cd; color: #856404; }}
                .screenshot-img {{ max-width: 150px; cursor: pointer; border-radius: 5px; }}
                .timestamp {{ color: #666; font-size: 0.85em; }}
                @media (max-width: 768px) {{
                    th, td {{ padding: 8px; font-size: 12px; }}
                    .stats {{ grid-template-columns: 1fr; }}
                }}
            </style>
        </head>
        <body>
            <div class="container">
                <div class="header">
                    <h1>🤖 E-Commerce Automation Test Suite</h1>
                    <p>Generated on {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}</p>
                </div>
                <div class="stats">
                    <div class="stat-card">
                        <div class="number">{total}</div>
                        <div class="label">Total Tests</div>
                    </div>
                    <div class="stat-card pass-count">
                        <div class="number">{passed}</div>
                        <div class="label">✅ Passed</div>
                    </div>
                    <div class="stat-card fail-count">
                        <div class="number">{failed}</div>
                        <div class="label">❌ Failed</div>
                    </div>
                    <div class="stat-card warn-count">
                        <div class="number">{warnings}</div>
                        <div class="label">⚠️ Warnings</div>
                    </div>
                </div>
                <div class="results">
                    <h2>Test Execution Details</h2>
                    <table>
                        <thead>
                            <tr>
                                <th>Time</th>
                                <th>Test Name</th>
                                <th>Status</th>
                                <th>Message</th>
                                <th>Screenshot</th>
                            </tr>
                        </thead>
                        <tbody>
        """
        
        for result in self.test_results:
            screenshot_html = f"<img src='{result['screenshot']}' class='screenshot-img' onclick='window.open(this.src)'>" if result['screenshot'] else "N/A"
            html += f"""
                            <tr>
                                <td class="timestamp">{result['timestamp']}</td>
                                <td><strong>{result['test_name']}</strong></td>
                                <td><span class="status-badge status-{result['status']}">{result['status']}</span></td>
                                <td>{result['message']}</td>
                                <td>{screenshot_html}</td>
                            </tr>
            """
        
        html += """
                        </tbody>
                    </table>
                </div>
            </div>
            <script>
                function showImage(src) {
                    window.open(src, '_blank');
                }
            </script>
        </body>
        </html>
        """
        
        report_file = os.path.join(self.report_dir, f"test_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.html")
        with open(report_file, 'w', encoding='utf-8') as f:
            f.write(html)
        
        return report_file