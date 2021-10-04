// Fix the Code or Make it better.

public class Calculator extends javax.swing.JFrame {

    public Calculator() {
        initComponents();
    }

    private void useOperator(String op) {
        operator = op;
        firstVal = Integer.parseInt(textField.getText());
        textField.setText("");
        textField1.setText(op);

    }

    private void calculate() {
        double calValue = 0;
        secondVal = Integer.parseInt(textField.getText());

        if (this.operator.equals("+")) {
            calValue = firstVal + secondVal;
        } else if (this.operator.equals("-")) {
            calValue = firstVal - secondVal;
        } else if (this.operator.equals("*")) {
            calValue = firstVal * secondVal;
        } else if (this.operator.equals("/")) {
            calValue = firstVal / secondVal;
        }
        textField.setText(calValue+"");
        

    }
    
    private void pressNumButton(String no){
    textField.setText(textField.getText()+no);
    }
    
    private void clearCal(){
    firstVal=0;
    secondVal=0;
    textField.setText("");
    textField1.setText("");
    }

    @SuppressWarnings("unchecked")
    // <editor-fold defaultstate="collapsed" desc="Generated Code">                          
    private void initComponents() {

        jPanel2 = new javax.swing.JPanel();
        textField1 = new javax.swing.JTextField();
        textField = new javax.swing.JTextField();
        jPanel1 = new javax.swing.JPanel();
        jButton5 = new javax.swing.JButton();
        jButton10 = new javax.swing.JButton();
        jButton14 = new javax.swing.JButton();
        jButton13 = new javax.swing.JButton();
        jButton12 = new javax.swing.JButton();
        jButton11 = new javax.swing.JButton();
        jButton15 = new javax.swing.JButton();
        jButton16 = new javax.swing.JButton();
        jButton9 = new javax.swing.JButton();
        jButton8 = new javax.swing.JButton();
        jButton7 = new javax.swing.JButton();
        jButton6 = new javax.swing.JButton();
        jButton2 = new javax.swing.JButton();
        jButton4 = new javax.swing.JButton();
        jButton3 = new javax.swing.JButton();
        jButton1 = new javax.swing.JButton();

        setDefaultCloseOperation(javax.swing.WindowConstants.EXIT_ON_CLOSE);

        jPanel2.setBackground(new java.awt.Color(255, 255, 255));
        jPanel2.setLayout(new org.netbeans.lib.awtextra.AbsoluteLayout());

        textField1.setFont(new java.awt.Font("Tahoma", 1, 12)); // NOI18N
        textField1.setBorder(null);
        jPanel2.add(textField1, new org.netbeans.lib.awtextra.AbsoluteConstraints(190, 10, 40, 39));

        textField.setFont(new java.awt.Font("Tahoma", 1, 12)); // NOI18N
        textField.setBorder(null);
        textField.setMargin(new java.awt.Insets(10, 2, 2, 2));
        jPanel2.add(textField, new org.netbeans.lib.awtextra.AbsoluteConstraints(10, 11, 180, 39));

        jPanel1.setLayout(new java.awt.GridLayout(4, 1));

        jButton5.setFont(new java.awt.Font("Tahoma", 1, 14)); // NOI18N
        jButton5.setText("7");
        jButton5.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                jButton5ActionPerformed(evt);
            }
        });
        jPanel1.add(jButton5);

        jButton10.setFont(new java.awt.Font("Tahoma", 1, 14)); // NOI18N
        jButton10.setText("8");
        jButton10.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                jButton10ActionPerformed(evt);
            }
        });
        jPanel1.add(jButton10);

        jButton14.setFont(new java.awt.Font("Tahoma", 1, 14)); // NOI18N
        jButton14.setText("9");
        jButton14.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                jButton14ActionPerformed(evt);
            }
        });
        jPanel1.add(jButton14);

        jButton13.setFont(new java.awt.Font("Tahoma", 1, 14)); // NOI18N
        jButton13.setText("\\");
            jButton13.addActionListener(new java.awt.event.ActionListener() {
                public void actionPerformed(java.awt.event.ActionEvent evt) {
                    jButton13ActionPerformed(evt);
                }
            });
            jPanel1.add(jButton13);

            jButton12.setFont(new java.awt.Font("Tahoma", 1, 14)); // NOI18N
            jButton12.setText("4");
            jButton12.addActionListener(new java.awt.event.ActionListener() {
                public void actionPerformed(java.awt.event.ActionEvent evt) {
                    jButton12ActionPerformed(evt);
                }
            });
            jPanel1.add(jButton12);

            jButton11.setFont(new java.awt.Font("Tahoma", 1, 14)); // NOI18N
            jButton11.setText("5");
            jButton11.addActionListener(new java.awt.event.ActionListener() {
                public void actionPerformed(java.awt.event.ActionEvent evt) {
                    jButton11ActionPerformed(evt);
                }
            });
            jPanel1.add(jButton11);

            jButton15.setFont(new java.awt.Font("Tahoma", 1, 14)); // NOI18N
            jButton15.setText("6");
            jButton15.addActionListener(new java.awt.event.ActionListener() {
                public void actionPerformed(java.awt.event.ActionEvent evt) {
                    jButton15ActionPerformed(evt);
                }
            });
            jPanel1.add(jButton15);

            jButton16.setFont(new java.awt.Font("Tahoma", 1, 14)); // NOI18N
            jButton16.setText("X");
            jButton16.addActionListener(new java.awt.event.ActionListener() {
                public void actionPerformed(java.awt.event.ActionEvent evt) {
                    jButton16ActionPerformed(evt);
                }
            });
            jPanel1.add(jButton16);

            jButton9.setFont(new java.awt.Font("Tahoma", 1, 14)); // NOI18N
            jButton9.setText("1");
            jButton9.addActionListener(new java.awt.event.ActionListener() {
                public void actionPerformed(java.awt.event.ActionEvent evt) {
                    jButton9ActionPerformed(evt);
                }
            });
            jPanel1.add(jButton9);

            jButton8.setFont(new java.awt.Font("Tahoma", 1, 14)); // NOI18N
            jButton8.setText("2");
            jButton8.addActionListener(new java.awt.event.ActionListener() {
                public void actionPerformed(java.awt.event.ActionEvent evt) {
                    jButton8ActionPerformed(evt);
                }
            });
            jPanel1.add(jButton8);

            jButton7.setFont(new java.awt.Font("Tahoma", 1, 14)); // NOI18N
            jButton7.setText("3");
            jButton7.addActionListener(new java.awt.event.ActionListener() {
                public void actionPerformed(java.awt.event.ActionEvent evt) {
                    jButton7ActionPerformed(evt);
                }
            });
            jPanel1.add(jButton7);

            jButton6.setFont(new java.awt.Font("Tahoma", 1, 14)); // NOI18N
            jButton6.setText("-");
            jButton6.addActionListener(new java.awt.event.ActionListener() {
                public void actionPerformed(java.awt.event.ActionEvent evt) {
                    jButton6ActionPerformed(evt);
                }
            });
            jPanel1.add(jButton6);

            jButton2.setFont(new java.awt.Font("Tahoma", 1, 14)); // NOI18N
            jButton2.setText("C");
            jButton2.addActionListener(new java.awt.event.ActionListener() {
                public void actionPerformed(java.awt.event.ActionEvent evt) {
                    jButton2ActionPerformed(evt);
                }
            });
            jPanel1.add(jButton2);

            jButton4.setFont(new java.awt.Font("Tahoma", 1, 14)); // NOI18N
            jButton4.setText("0");
            jButton4.addActionListener(new java.awt.event.ActionListener() {
                public void actionPerformed(java.awt.event.ActionEvent evt) {
                    jButton4ActionPerformed(evt);
                }
            });
            jPanel1.add(jButton4);

            jButton3.setFont(new java.awt.Font("Tahoma", 1, 14)); // NOI18N
            jButton3.setText("=");
            jButton3.addActionListener(new java.awt.event.ActionListener() {
                public void actionPerformed(java.awt.event.ActionEvent evt) {
                    jButton3ActionPerformed(evt);
                }
            });
            jPanel1.add(jButton3);

            jButton1.setFont(new java.awt.Font("Tahoma", 1, 14)); // NOI18N
            jButton1.setText("+");
            jButton1.addActionListener(new java.awt.event.ActionListener() {
                public void actionPerformed(java.awt.event.ActionEvent evt) {
                    jButton1ActionPerformed(evt);
                }
            });
            jPanel1.add(jButton1);

            javax.swing.GroupLayout layout = new javax.swing.GroupLayout(getContentPane());
            getContentPane().setLayout(layout);
            layout.setHorizontalGroup(
                layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                .addComponent(jPanel1, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                .addComponent(jPanel2, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
            );
            layout.setVerticalGroup(
                layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                .addGroup(layout.createSequentialGroup()
                    .addComponent(jPanel2, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                    .addComponent(jPanel1, javax.swing.GroupLayout.DEFAULT_SIZE, 327, Short.MAX_VALUE))
            );

            pack();
        }// </editor-fold>                        

    private void jButton4ActionPerformed(java.awt.event.ActionEvent evt) {                                         
        pressNumButton("0");
    }                                        

    private void jButton9ActionPerformed(java.awt.event.ActionEvent evt) {                                         
     pressNumButton("1");
    }                                        

    private void jButton8ActionPerformed(java.awt.event.ActionEvent evt) {                                         
     pressNumButton("2");
        
    }                                        

    private void jButton7ActionPerformed(java.awt.event.ActionEvent evt) {                                         
     pressNumButton("3");
    }                                        

    private void jButton12ActionPerformed(java.awt.event.ActionEvent evt) {                                          
     pressNumButton("4");
    }                                         

    private void jButton11ActionPerformed(java.awt.event.ActionEvent evt) {                                          
     pressNumButton("5");
    }                                         

    private void jButton15ActionPerformed(java.awt.event.ActionEvent evt) {                                          
     pressNumButton("6");
    }                                         

    private void jButton5ActionPerformed(java.awt.event.ActionEvent evt) {                                         
       pressNumButton("7");
    }                                        

    private void jButton10ActionPerformed(java.awt.event.ActionEvent evt) {                                          
       pressNumButton("8");
    }                                         

    private void jButton14ActionPerformed(java.awt.event.ActionEvent evt) {                                          
        pressNumButton("9");
    }                                         

    private void jButton1ActionPerformed(java.awt.event.ActionEvent evt) {                                         
        useOperator("+");
    }                                        

    private void jButton6ActionPerformed(java.awt.event.ActionEvent evt) {                                         
       useOperator("-");
    }                                        

    private void jButton16ActionPerformed(java.awt.event.ActionEvent evt) {                                          
       useOperator("*");
    }                                         

    private void jButton13ActionPerformed(java.awt.event.ActionEvent evt) {                                          
       useOperator("/");
    }                                         

    private void jButton2ActionPerformed(java.awt.event.ActionEvent evt) {                                         
       clearCal();
    }                                        

    private void jButton3ActionPerformed(java.awt.event.ActionEvent evt) {                                         
    calculate();
    }                                        

    public static void main(String args[]) {

        try {
            for (javax.swing.UIManager.LookAndFeelInfo info : javax.swing.UIManager.getInstalledLookAndFeels()) {
                if ("Windows".equals(info.getName())) {
                    javax.swing.UIManager.setLookAndFeel(info.getClassName());
                    break;
                }
            }
        } catch (ClassNotFoundException ex) {
            java.util.logging.Logger.getLogger(Calculator.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (InstantiationException ex) {
            java.util.logging.Logger.getLogger(Calculator.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (IllegalAccessException ex) {
            java.util.logging.Logger.getLogger(Calculator.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (javax.swing.UnsupportedLookAndFeelException ex) {
            java.util.logging.Logger.getLogger(Calculator.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        }

        java.awt.EventQueue.invokeLater(new Runnable() {
            public void run() {
                new Calculator().setVisible(true);
            }
        });
    }

    // Variables declaration - do not modify                     
    private javax.swing.JButton jButton1;
    private javax.swing.JButton jButton10;
    private javax.swing.JButton jButton11;
    private javax.swing.JButton jButton12;
    private javax.swing.JButton jButton13;
    private javax.swing.JButton jButton14;
    private javax.swing.JButton jButton15;
    private javax.swing.JButton jButton16;
    private javax.swing.JButton jButton2;
    private javax.swing.JButton jButton3;
    private javax.swing.JButton jButton4;
    private javax.swing.JButton jButton5;
    private javax.swing.JButton jButton6;
    private javax.swing.JButton jButton7;
    private javax.swing.JButton jButton8;
    private javax.swing.JButton jButton9;
    private javax.swing.JPanel jPanel1;
    private javax.swing.JPanel jPanel2;
    private javax.swing.JTextField textField;
    private javax.swing.JTextField textField1;
    // End of variables declaration                   
    private double firstVal;
    private double secondVal;
    private String operator;
}
